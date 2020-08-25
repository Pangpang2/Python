from urllib3.exceptions import ReadTimeoutError, ConnectTimeoutError
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.queue import QueueItem
import time


class JenkinsCaller:

    def __init__(self, environment=None):
        self.configs = {'username': "api-user",
                        'password': "ondemand1!",
                        'baseurl': "http://stg-df-jobs1.internetbrands.com:8080",
                        'nodegroup': '38'}

    def get_server_instance(self):
        wait_time = 2
        while True:
            try:
                server = Jenkins(self.configs["baseurl"], username=self.configs["username"],
                                password=self.configs["password"])
                break
            except Exception as e:
                if isinstance(e, ReadTimeoutError) or isinstance(e, ConnectTimeoutError):
                    print(str(e))
                    time.sleep(wait_time)
                    wait_time *= 2
            if wait_time > 30:
                raise Exception('after waiting 30 secs with 2 sec break, still cannot connect to jenkins server')
        return server

    def _run_jenkins_job(self, build_params, job_path, files=None, check_delay=5, block=True):
        """ run jenkins job specified by the job_path with build_params

        :param dict build_params: parameters to customize the jenkins job run
        :param str job_path: the jenkins job path relative to the jenkins root path, for instance:
        'Common_Jobs/Staging_Campaign_Scheduler'
        :param int check_delay:
        :param bool block:

        :rtype: QueueItem
        :return: the queue item that describes the launched job info
        """
        server = JenkinsCaller.get_server_instance(self)
        job = server[job_path]
        print("Running Jenkins Service: " + job_path)
        if files:
            qi = job.invoke(build_params=build_params, files=files)
        else:
            qi = job.invoke(build_params=build_params)
        if block:
            JenkinsCaller._block_and_track_progress(qi, check_delay)
        return qi

    @staticmethod
    def _block_and_track_progress(qi, delay=5):
        """ this function is supposed to be called right after job is kicked off,
        blocks execution for the current thread, provide tracking information of the job

        :param QueueItem qi:
        :rtype: QueueItem
        :return: the queue item
        """
        print("Jenkins queue id: " + str(qi.queue_id))

        print("Jenkins job queued, queue_id={queue_id}".format(queue_id=qi.queue_id))
        qi.block_until_building()

        print("Jenkins build number: " + str(qi.get_build_number()))

        print("Jenkins job started, queue_id={queue_id}, build_no={build_no}, job_name={job_name}".
                 format(queue_id=qi.queue_id, build_no=qi.get_build_number(), job_name=qi.get_job_name()))
        qi.block_until_complete(delay)
        print("Jenkins job finished, queue_id={queue_id}, build_no={build_no}, job_name={job_name}".
                 format(queue_id=qi.queue_id, build_no=qi.get_build_number(), job_name=qi.get_job_name()))


def run_assign_planid_reminder_2(nodegroup='38', type='appointment', tag='staging'):

    build_params_appointment = {'NODEGROUP': nodegroup,
                                'TYPE': type,
                                'TAG': tag}

    job_path = "Common_Jobs/Assign_PlanId_Reminders_2.0"

    caller = JenkinsCaller()
    caller._run_jenkins_job(build_params=build_params_appointment, job_path=job_path)

from threading import Thread

def sub_thread(num):
    print('This is the {0} thread' + num)

# if __name__ == '__main__':
# #     print('Main thread')
# #     my_thread = Thread(target=sub_thread, args=1)
# #     my_thread.join()
if __name__ == '__main__':
    for i in range(1,16):
        print(i)

    for i in range(1,16):
        upload_list = []
        for username in range(135000001,135000101,1):
            upload_info = {}
            # print('Round:' + str(i))
            auth_token = str(i) + str(username)
            # print('username:' + str(username))
            # print(auth_token)
            # gz_file = compress_to_gz_file("./data/test.xml")
            # print(gz_file)
            upload_info['username'] = str(username)
            upload_info['token'] = auth_token
            upload_info['file'] = 'test.xml' + str(i) + str(username)
            upload_list.append(upload_info)

            if len(upload_list)%10 == 0:
                for upload_info in upload_list:
                    print('Upload round {0} for {1}'.format(i, upload_info['username']))
                    print(upload_info['token'] +'-----' + upload_info['file'])
                    # response = upload_xml(up_url, upload_info['auth'], upload_info[file])
                    # print(response.status_code)
                upload_list = []
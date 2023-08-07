#pip install speedtest-cli
try:
    import speedtest
    test = speedtest.Speedtest()
    test.get_servers()
    print("Choosing the best Server available..........")
    best = test.get_best_server()
    download_result = test.download()
    upload_result = test.upload()
    print("-------------YOUR INTERNET SPEED TEST RESULT-----------------")
    print(f"DOWNLOAD RESULT :{download_result / 1024 / 1024:.2f} MB PER SECOND ")
    print(f"UPLOAD RESUTL :{upload_result /1024 / 1024:.2f}MB PER SECOND")
    print("-----------You can get a png result from this Link-----------")
    print(test.results.share())
    i = input("Press any key to exit")
except Exception as e:
    print("Sorry Sir I am not able to check your internet speed. As because there is no Internet or it is unstable.")
    print(e)
    i = input("Press any key to exit")

from pymongo import MongoClient
from helper import calculate_app_top_5, calculate_user_top_5
from dataservice import DataService
import time
def main():
    try:
        client = MongoClient('localhost', 27017)
        DataService.init(client)

        
        # work flow
        user_download_history = DataService.retrieve_user_download_history()
        app_info = DataService.retrieve_app_info()

        # print("Calculating Top 5 related apps for apps...")
        # start = time.clock()
        # for app in app_info.keys():
        #     # print(app)
        #     calculate_app_top_5(app, user_download_history.values())
        # # calculate_top_5('C10107104', user_download_history.values())
        # end = time.clock()

        # print "time elapsed = " + str(end - start)

        print("Calculating Top 5 recommended apps for users...")

        start = time.clock()
        for user_id, download_history in user_download_history.iteritems():
            # print(app)
            calculate_user_top_5(user_id, download_history, user_download_history.values())
        # calculate_top_5('C10107104', user_download_history.values())
        end = time.clock()

        print "time elapsed = " + str(end - start)

    except Exception as e:
        print(e)
    finally:
        # clean up work
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    main()
# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    import urllib2
    # If you are using Python 3+, import urllib instead of urllib2

    import json

    url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Hillary%20Clinton&prop=revisions&rvprop=timestamp|user|size&rvlimit=5&format=json'
    #api_key = 'abc123' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json'}

    req = urllib2.Request(url,None,headers)

    try:
        response = urllib2.urlopen(req)
        result = response.read()


        print("url returned")
        #print(result)

        wp_data = json.loads(result)
        print("json read as")
        print(wp_data)

        print("object here")
        print(wp_data['query']['pages'])
        print("object here")
        print(wp_data['query']['pages'].values()[0])


    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))
    finally:

        rev = wp_data['query']['pages'].values()[0]['revisions']

        df = pd.DataFrame()

        # Execution logic goes here
        #print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))
        #for x in rev:
        #    ln = pd.DataFrame(x)
        #    df.append(ln)

        print('Appended DataFrame #1:\r\n\r\n{0}'.format(df))


        wf = pd.DataFrame(wp_data['query']['pages'].values()[0]['revisions'])
        print('wiki frame wf:\r\n\r\n{0}'.format(wf))

        #df = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
        #                   'D': ['D2', 'D3', 'D6', 'D7'],
        #                   'F': ['F2', 'F3', 'F6', 'F7']})


        #dataframe1.append(df)

        #print('Appended pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))

        # If a zip file is connected to the third input port is connected,
        # it is unzipped under ".\Script Bundle". This directory is added
        # to sys.path. Therefore, if your zip file contains a Python file
        # mymodule.py you can import it using:
        # import mymodule

        # Return value must be of a sequence of pandas.DataFrame
    return wf #dataframe1,
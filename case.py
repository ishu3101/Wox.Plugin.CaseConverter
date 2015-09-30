import json
import webbrowser
import os

def addToClipBoard(context, text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def query(input):
    results = []
    res = {}

    # get the keyword.
    keyword = input.split()[0]
    # get the query into an array.
    t = input.split()[1:]
    delimiter = ' '
    # join the array with a space in between the elements.
    query = delimiter.join(t)

    print (query)
    variations = {
      'lowercase': query.lower(),
      'uppercase': query.upper(),
      'titlecase': query.title()
    }

    for key, value in sorted(variations.items()):
        title = value
        subTitle = key

        res["Title"] = title
        res["SubTitle"] = "Convert to " + subTitle
        res["ActionName"] = "addToClipBoard"
        res["IcoPath"] = subTitle + ".png"
        res["ActionPara"] = title
        results.append(dict(res))
    # pretty prints json output
    return json.dumps(results,sort_keys=True,indent=4, separators=(',', ': '))

def openUrl(context,url):
    webbrowser.open(url)

if __name__ == "__main__":
    print query("movie geo")

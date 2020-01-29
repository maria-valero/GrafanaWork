import json
import sys

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

print 'MAC Address for Dashboard:', str(sys.argv[1])
print 'Dashboard to copy:', str(sys.argv[2])
dash_tc=str(sys.argv[2])
mac=str(sys.argv[1])
mac_r=mac.replace(":","-")

with open(dash_tc) as json_file:
    data = json.load(json_file)
    datacopy = data;
    
    #Panel 0 Heart Rate
    print(datacopy['dashboard']['panels'][0]['targets'][0]['tags'][0]['value'])
    value = datacopy['dashboard']['panels'][0]['targets'][0]['tags'][0]['value']
    newvalue = mac
    datacopy['dashboard']['panels'][0]['targets'][0]['tags'][0]['value'] = newvalue
    
    #Panel 1 
    print(datacopy['dashboard']['panels'][1]['targets'][0]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][0]['query']
    newvalue = value[:46]+mac+value[63:]
    datacopy['dashboard']['panels'][1]['targets'][0]['query'] = newvalue

    print(datacopy['dashboard']['panels'][1]['targets'][1]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][1]['query']
    newvalue = value[:46]+mac+value[63:]
    datacopy['dashboard']['panels'][1]['targets'][1]['query'] = newvalue

    print(datacopy['dashboard']['panels'][1]['targets'][2]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][2]['query']
    newvalue = value[:50]+mac+value[67:]
    datacopy['dashboard']['panels'][1]['targets'][2]['query'] = newvalue

    print(datacopy['dashboard']['panels'][1]['targets'][3]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][3]['query']
    newvalue = value[:54]+mac+value[71:]
    datacopy['dashboard']['panels'][1]['targets'][3]['query'] = newvalue

    print(datacopy['dashboard']['panels'][1]['targets'][4]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][4]['query']
    newvalue = value[:59]+mac+value[76:]
    datacopy['dashboard']['panels'][1]['targets'][4]['query'] = newvalue

    print(datacopy['dashboard']['panels'][1]['targets'][5]['query'])
    value = datacopy['dashboard']['panels'][1]['targets'][5]['query']
    newvalue = value[:61]+mac+value[78:]
    datacopy['dashboard']['panels'][1]['targets'][5]['query'] = newvalue

    #Panel 2
    print(datacopy['dashboard']['panels'][2]['targets'][0]['query'])
    value = datacopy['dashboard']['panels'][2]['targets'][0]['query']
    newvalue = value[:52]+mac+value[69:]
    datacopy['dashboard']['panels'][2]['targets'][0]['query'] = newvalue
    
    #Panel 3
    print(datacopy['dashboard']['panels'][3]['targets'][0]['query'])
    value = datacopy['dashboard']['panels'][3]['targets'][0]['query']
    newvalue = value[:53]+mac+value[70:]
    datacopy['dashboard']['panels'][3]['targets'][0]['query'] = newvalue
    
    #Panel 4 Respiration Rate
    print(datacopy['dashboard']['panels'][4]['targets'][0]['tags'][0]['value'])
    newvalue = mac
    datacopy['dashboard']['panels'][4]['targets'][0]['tags'][0]['value'] = newvalue

    #Panel 5 On/Off Bed and Detecting 
    print(datacopy['dashboard']['panels'][5]['targets'][0]['tags'][0]['value'])
    newvalue = mac
    datacopy['dashboard']['panels'][5]['targets'][0]['tags'][0]['value'] = newvalue

    #Panel 6 Fall down
    print(datacopy['dashboard']['panels'][6]['targets'][0]['tags'][0]['value'])
    newvalue = mac
    datacopy['dashboard']['panels'][6]['targets'][0]['tags'][0]['value'] = newvalue

    #Panel 7 QC
    print(datacopy['dashboard']['panels'][7]['targets'][0]['tags'][0]['value'])
    newvalue = mac
    datacopy['dashboard']['panels'][7]['targets'][0]['tags'][0]['value'] = newvalue

    #Panel 8 Raw Data
    print(datacopy['dashboard']['panels'][8]['targets'][0]['tags'][0]['value'])
    newvalue = mac
    datacopy['dashboard']['panels'][8]['targets'][0]['tags'][0]['value'] = newvalue

    print(datacopy['dashboard']['title'])
    value = datacopy['dashboard']['title']
    newvalue = value[:17]+mac
    datacopy['dashboard']['title'] = newvalue
        
    print(datacopy['dashboard']['uid'])
    newuid = mac.replace(":","")
    datacopy['dashboard']['uid'] = newuid
    
    print(datacopy['meta']['url'])
    value = datacopy['meta']['url']
    nth=find_nth(value, "/", 3) 
    newvalue = value[:3]+newuid+value[nth:nth+15]+mac_r
    print newvalue
    datacopy['meta']['url']=newvalue

    print(datacopy['meta']['slug'])
    value = datacopy['meta']['slug']
    newvalue = value[:14]+mac_r+value[31:]
    datacopy['meta']['slug'] = newvalue
   
    print(datacopy['dashboard']['gnetId'])
    newvalue = 'null'
    datacopy['dashboard']['gnetId'] = newvalue

    print(datacopy['dashboard']['id'])
    newvalue = 'null'
    datacopy['dashboard']['id']=newvalue

    savein = "dashboards/"+"bed-dashboard-"+mac_r+".json"
    print savein
    with open(savein, 'w') as outfile:
       json.dump(data, outfile)

'''

assumptions:

APICommand (object)
APICommand(Args: API_KEY)

data members:

self.APIKey
self.org_id
self.networks
self.network_id
self.email

maintence start => maintence_end

NOTE: Do not TEST HOT!
        TEST with dummy vars to make sure loop works.

__init__(self,maintence_start,maintence_end):
    if maintenence start != null:
        alerts muted
        # clock logic
        while not exit: - for any x not > maintence_end, no action
                        for any x > maintence_end, one action, API Call, then exit
            wait(1000) (only check once a second)
            if time > maintence_end:
                alerts unmute
                exit True
            else: #wait

get org_id
get_networks
get_adminEmail
get_alerts (?)
alerts_off
alerts_on


when called in main backend:

main APICommand = new APICommand(APIKEY) (C OMEGALUL)
main.alerts_off(start)
main.alerts_on(stop)
    larger command -> do_maintence(start,stop)




for x in APICommand[all objects] -> sys.clock calls
    == used for timing
    -> API on/off commands



suppose time x, where start > x < end

payload = json.read(somefile)

'''
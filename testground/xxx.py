result = {
    "id":"9089046963601126226",
    "insertTime":"2022-07-29T09:41:33.330-07:00",
    "kind":"compute#operation",
    "name":"operation-1659112892789-5e4f4529df11e-b0ced6ff-056402fc",
    "operationType":"stop",
    "progress":0,
    "selfLink":"https://www.googleapis.com/compute/v1/projects/named-aspect-356717/zones/europe-central2-a/operations/operation-1659112892789-5e4f4529df11e-b0ced6ff-056402fc",
    "startTime":"2022-07-29T09:41:33.343-07:00",
    "status":"RUNNING",
    "targetId":"5546540169583662850",
    "targetLink":"https://www.googleapis.com/compute/v1/projects/named-aspect-356717/zones/europe-central2-a/instances/swinka-vm",
    "user":"tonieja@named-aspect-356717.iam.gserviceaccount.com",
    "zone":"https://www.googleapis.com/compute/v1/projects/named-aspect-356717/zones/europe-central2-a"
    }

import googleapiclient.discovery

def stop_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    instances = compute.instances()
    instance_names = []

    for instance in instances:
        if instance["status"] == "RUNNING":
            data_to_split = result["targetLink"]
            instance_names.append(data_to_split.split('/')[-1])

    for name in instance_names:
        compute.instances().stop(project='named-aspect-356717', zone='europe-central2-a', instance=name).execute()
    
    return instance_names
from torch.utils.data import Dataset
import json
import os

class ExpertDataset(Dataset):
    """Dataset of RGB images, driving affordances and expert actions"""
    def __init__(self, data_root):
        self.data_root = data_root
        # Your code here
        #my code starts here
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        world = client.load_world('Town01')

        temp = {
            "speed" : 0.0,
            "speed" : 0.0,
            "speed" : 0.0,
            "throttle" : 0.0,
            "brake" : 0.0,
            "steer" : 0,
            "command" : 0.0,
            "route dist" : 0.0,
            "route angle" : 0.0,
            "lane dist" : 0.0,
            "lane angle" : 0.0,
            "hazard" : True,
            "hazard dist" : 0.0,
            "tl state" : 0, 
            "is junction" : True
        }

        y = json.loads(temp)
    
        
        #my code end here



#collect_data.py  ----->  json_path = os.path.join(self.config["data_dir"], 
#mappings.py    --------> mappings.p

    def __getitem__(self, index):
        
        pass

         #my code end here


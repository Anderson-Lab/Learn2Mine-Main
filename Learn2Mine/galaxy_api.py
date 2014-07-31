#!/usr/bin/env python
from common import display
from common import submit

"""
# ---------------------------------------------- #
# PARKLAB, Author: RPARK
# ---------------------------------------------- #

Execute workflows from the command line.
Example calls:
python workflow_execute.py <api_key> <galaxy_url>/api/workflows <workflow_id> 'hist_id=<history_id>' '38=hda=<file_id>' 'param=tool=name=value'
python workflow_execute_parameters.py <api_key> http://localhost:8080/api/workflows 1cd8e2f6b131e891 'Test API' '69=ld=a799d38679e985db' '70=ld=33b43b4e7093c91f' 'param=peakcalling_spp=aligner=bowtie' 'param=bowtie_wrapper=suppressHeader=True' 'param=peakcalling_spp=window_size=1000'
"""


#usage: array containing: key url workflow_id history step=src=dataset_id
def workflow_execute_parameters(*argv):
    data = {}
    data['workflow_id'] = argv[2]
    data['history'] = argv[3]
    data['ds_map'] = {}

    #########################################################
    ### Trying to pass in parameter for my own dictionary ###
    data['parameters'] = {}

    # DBTODO If only one input is given, don't require a step
    # mapping, just use it for everything?
    for v in argv[4:]:
        print("Multiple arguments ");
        print(v);

        try:
            step, src, ds_id = v.split('=');
            data['ds_map'][step] = {'src':src, 'id':ds_id};

        except ValueError:
            print("VALUE ERROR:");
            #wtype, wtool, wparam, wvalue = v.split('=');
            fields = v.split('=');
            wtype,wtool,wparam = fields[0],fields[1],fields[2]
            wvalue = "=".join(fields[3:len(fields)])
            try:
                data['parameters'][wtool] = {'param':wparam, 'value':wvalue}
            except ValueError:
                print("TOOL ID ERROR:");

    print data 
    return submit( argv[0], argv[1], data, return_formatted=False)

def display_result(*argv):
    return display( *argv[0:2] , return_formatted=False)


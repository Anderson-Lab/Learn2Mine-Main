from bioblend.galaxy import GalaxyInstance

gi = GalaxyInstance(url='http://localhost:8081/learn2mine', key='a8fafae3769c28e62536c3717372bcba', email='datascienceresearch@gmail.com')

for history in gi.histories.get_histories():
  history_id = history['id']
  history2 = gi.histories.show_history(history_id)#, contents=True,details=True)
  for ds_id in history2['state_ids']['ok']:
##print gi.datasets.show_dataset('982839f864e31dec')
	print gi.histories.show_dataset_provenance(history_id,ds_id)

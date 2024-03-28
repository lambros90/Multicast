from flask import Flask, request, render_template, url_for, redirect, json
from datetime import date
import os
app = Flask(__name__)

@app.route('/github', methods = ['POST', 'GETq'])
def github_hook():
	if request.method == 'POST':
		update_repo()
		return "completed"
	else:
		return ('wrong request')
		
def update_repo():
	today = date.today()
	
	os.system('cd /home/ubuntu/xrdocs/ncs5500/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ncs5500 repo was updated')

	os.system('cd /home/ubuntu/xrdocs/ncs5500/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ncs5500 repo was updated')

	os.system('cd /home/ubuntu/xrdocs/tdm2ip/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('tdm2ip repo was updated')

	os.system('cd /home/ubuntu/xrdocs/tdm2ip/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('tdm2ip repo was updated')

	os.system('cd /home/ubuntu/xrdocs/telemetry/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('telemetry repo was updated')

	os.system('cd /home/ubuntu/xrdocs/telemetry/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('telemetry repo was updated')

	os.system('cd /home/ubuntu/xrdocs/device-lifecycle/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('device-lifecycle repo was updated')

	os.system('cd /home/ubuntu/xrdocs/device-lifecycle/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('device-lifecycle repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cloud-scale-networking/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cloud-scale-networking repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cloud-scale-networking/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cloud-scale-networking repo was updated')

	os.system('cd /home/ubuntu/xrdocs/application-hosting/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('application-hosting repo was updated')

	os.system('cd /home/ubuntu/xrdocs/application-hosting/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('application-hosting repo was updated')

	os.system('cd /home/ubuntu/xrdocs/automation/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('automation repo was updated')

	os.system('cd /home/ubuntu/xrdocs/automation/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('automation repo was updated')

	os.system('cd /home/ubuntu/xrdocs/programmability/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('programmability repo was updated')

	os.system('cd /home/ubuntu/xrdocs/programmability/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('programmability repo was updated')

	os.system('cd /home/ubuntu/xrdocs/multicast/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('multicast repo was updated')

	os.system('cd /home/ubuntu/xrdocs/multicast/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('multicast repo was updated')

	os.system('cd /home/ubuntu/xrdocs/packet-fronthaul/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('packet-fronthaul repo was updated')

	os.system('cd /home/ubuntu/xrdocs/packet-fronthaul/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('packet-fronthaul repo was updated')

	os.system('cd /home/ubuntu/xrdocs/8000/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

	os.system('cd /home/ubuntu/xrdocs/8000/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('8000 repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cnbng/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cnbg repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cnbng/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cnbg repo was updated')

	os.system('cd /home/ubuntu/xrdocs/asr9k/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('asr9k repo was updated')

	os.system('cd /home/ubuntu/xrdocs/asr9k/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('asr9k repo was updated')

	os.system('cd /home/ubuntu/xrdocs/security/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('security repo was updated')

	os.system('cd /home/ubuntu/xrdocs/security/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('security repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cisco-service-layer/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cisco-service-layer repo was updated')

	os.system('cd /home/ubuntu/xrdocs/cisco-service-layer/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cisco-service-layer was updated')

	os.system('cd /home/ubuntu/xrdocs/segment-routing/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('segment-routing repo was updated')

	os.system('cd /home/ubuntu/xrdocs/segment-routing/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('segment-routing repo was updated')

	os.system('cd /home/ubuntu/xrdocs/ztp/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ztp repo was updated')

	os.system('cd /home/ubuntu/xrdocs/ztp/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('ztp repo was updated')

	os.system('cd /home/ubuntu/xrdocs/virtual-routing/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('cnbg repo was updated')

	os.system('cd /home/ubuntu/xrdocs/virtual-routing/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('virtual-routing repo was updated')

	os.system('cd /home/ubuntu/xrdocs/xrdocs.github.io/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('xrdocs.github.io repo was updated')

	os.system('cd /home/ubuntu/xrdocs/xrdocs.github.io/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('xrdocs.github.io repo was updated')

	os.system('cd /home/ubuntu/xrdocs/design/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('design repo was updated')

	os.system('cd /home/ubuntu/xrdocs/design/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('design repo was updated')

	os.system('cd /home/ubuntu/xrdocs/routed-pon/ && git pull origin gh-pages && cd _data && git pull origin master && \
		cd .. && git add _data/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('routed-pon repo was updated')

	os.system('cd /home/ubuntu/xrdocs/routed-pon/ && cd images/avatars && git pull origin master && \
		cd ../.. && git add images/avatars/ . && git commit -m "subrepo update {0}" && git push origin gh-pages'.format(today))
	print ('routed-pon repo was updated')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7777, debug=True)

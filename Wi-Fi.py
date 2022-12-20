import os
def monitoring(server_ip):
    cmd = "ping -c 30 %s" % server_ip
    p = os.popen(cmd)
    info = p.read()
    p.close()
    re_lost_str = '(\d+)% packet loss'
    lost_packet = int(self.re.search(re_lost_str, info).group(1))
    if lost_packet > 30:
        deal_error(info)

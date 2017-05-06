from get_content import *

def get_json(end):
    start_ip = page.find('IP Address:', end)
    start_ip = page.find('">', start_ip)
    start_ip += 2
    end_ip = page.find('</', start_ip)
    ip = page[start_ip:end_ip]
    start_pt = page.find('Port', end_ip) + 7
    end_pt = page.find('</', start_pt)
    pt = page[start_pt:end_pt]
    start_pw = page.find('Password', end_pt)
    start_pw = page.find('">', start_pw) + 2
    end_pw = page.find('</s', start_pw)
    pw = page[start_pw:end_pw]
    start_md = page.find('Method', end_pw) + 7
    end_md = page.find('</h', start_md)
    md = page[start_md:end_md]
    return ip,pt,pw,md,end_md

def save_json(ip,pt,pw,md,x):
    file = open('gui-config.json', 'a')
    if x == 0:
        file.write("{\n\t\"configs\": [\n")
    file.write("\t\t{\n\t\t\t\"method\": " +'"'+ md +'"'+',\n\t')
    file.write("\t\t\"password\":" + '"'+pw + '"'+',\n\t')
    file.write("\t\t\"remarks\": " + '"'+ip[2:4]+ip[0:1]+'"'+',\n\t')
    file.write("\t\t\"server\": " + '"'+ip + '"'+',\n\t')
    file.write("\t\t\"server_port\": "+ pt)
    if x == 8:
        file.write("\n\t\t}\n\t],")
        file.write('\n\t"localPort": 1080,\n\t"shareOverLan": false\n}')
    else:
        file.write("\n\t\t},\n")
    file.close()

def main():
    end = 0
    file = open('gui-config.json', 'w')
    file.close()
    chose = input('以二维码还是文件保存？(qr or json):')
    if chose == 'json':
        for x in range(9):
            ip,pt,pw,md,end = get_json(end)
            save_json(ip,pt,pw,md,x)
    elif chose == 'qr':
        for x in range(9):
            if x == 0: end_p = 0
            img = 'http://xyz.ishadow.online/'
            start_p = page.find('img/qr/', end_p)
            end_p = page.find('"', start_p)
            img_t = img + page[start_p:end_p]
            im = requests.get(img_t)
            open(page[start_p+7:end_p],'wb').write(im.content)
            print('第%d张图片保存完成...'%(x+1))
            start_p = end_p

if __name__ == "__main__":
    main()

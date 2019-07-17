# encoding: utf-8



import os
import time

class TimeUtils():
    def get_curr_date(self):
        return time.strftime('%Y%m%d',time.localtime(time.time()))
    def get_curr_time(self):
        return time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))


class LogUtils():
    def info(self,title,content):
        self._log('info',title,content)
        return None
    def warn(self,title,content):
        self._log('warning',title,content)
        return None
    def err(self,title,content):
        self._log('error', title, content)
        return None

    def _log(self,level,title,content):
        curr_date=TimeUtils().get_curr_date()
        log_file_name=curr_date+level+'.txt'
        log_content='{} | title:() | content:{}'.format(level,title,content)
        print(log_content)
        try:
            with open(os.path.join('logs/',log_file_name),'a',encoding='utf8') as wf:
                wf.write(log_content+'|'+TimeUtils.get_curr_time()+'\n')
        except Exception as err:
            return None
        return None

if __name__ == '__main__':
    print('test')
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import os

app = Flask(__name__,static_url_path='')
os.chdir('C:/Users/胡尚志/Desktop/igem-website/HP/data')
with open('.name_list.txt','r') as f:#read name existed
        names_exist = f.readlines()
        names_exist  = [name.replace('\n','') for name in names_exist]
        currentnumber=  len(names_exist)-1
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def contact():
    return render_template('submit.html')
@app.route('/search/')
def search():
    with open('.name_list.txt','r') as f:#read name existed
        names_exist = f.readlines()
        names_exist  = [name.replace('\n','') for name in names_exist]
        currentnumber=  len(names_exist)-1

    return render_template('search.html',currentnumber=currentnumber)

@app.route('/search/<search_result>')
def _result(search_result):
    os.chdir('C:/Users/胡尚志/Desktop/igem-website/HP/data')
    with open(search_result+'.txt','r') as f:
        _result=eval(f.read())
                #with open('test.txt','w') as f:
                #    f.write(str(search_result))

    os.chdir('C:/Users/胡尚志/Desktop/igem-website/HP/commit')
    try:
    	with open(search_result+'.txt','r') as f:
    		commits = f.readlines()
    	commits = [commit.replace('\n','') for commit in commits]
    except:
    	commits = ['No commits']
    	f = open(search_result+'.txt','w')
    	f.close()
    return render_template('results.html',commits = commits, results=[_result])


@app.route('/search/',methods=['POST'])
def commit_process():
    _name = request.referrer.split('/')[-1]

    # os.chdir('D:/ShanghaiTech/iGEM-jamboree/software/HP/data')
    # with open(_name+'.txt','r') as f:
    #     _result=eval(f.read())

    os.chdir('C:/Users/胡尚志/Desktop/igem-website/HP/commit')
    #with open('test.txt','w') as f:
    #    f.write(str(dir(request)))
    #    for method in dir(request):
    #       f.write('/n'+str(method)+':'+str(eval('request.'+method)))

    with open(_name+'.txt','a') as f:
    	f.write(request.form.to_dict()['text']+'\n')
    # with open(_name+'.txt','r') as f:
    # 	commits = f.readlines()
    # 	commits = [commit.replace('\n','') for commit in commits]
    # return render_template('results.html',commits = commits, results=[_result])
    return redirect('/search/'+_name)

@app.route('/',methods=['POST'])
def form_process():
    os.chdir('C:/Users/胡尚志/Desktop/igem-website/HP/data')
    #with open('test.txt','w') as f:
    #    f.write(str(dir(request)))
        #for method in dir(request):
        #    f.write('/n'+str(method)+':'+str(eval('request.'+method)))
    #    f.write(str(dict(request.form)))
    from_place = dict(request.form)['submit'][0]#get the page from(submit or search)
    with open('.name_list.txt','r') as f:#read name existed
        names_exist = f.readlines()
        names_exist  = [name.replace('\n','') for name in names_exist]
        currentnumber=  len(names_exist)+1


    if from_place == 'Submit Message':
        item_dic = request.form.to_dict()
        if not item_dic['name']  in names_exist:
            with open('.name_list.txt','a') as f: #if name not exist,addable
                f.write(str(item_dic['name'])+'\n')
        else:
            return render_template('submit.html',result='Failed, name existed!')
        with open(item_dic['name']+'.txt','w') as f:
            #f.write(str(dir(request.form)))
            f.write(str(item_dic))
        return render_template('submit.html',result='Submit successed!')

    elif from_place == 'search':
        search_key = request.form['name']
        search_key_dict = {}
        for query_key in ['name','sequence','username','description']:
            try:
                query_rule = request.form[query_key]
                if len(query_rule):
                    search_key_dict[query_key]=query_rule
            except Exception as e:
                pass
        with open('C:/Users/胡尚志/Desktop/igem-website/HP/data/log.txt', 'a') as log_f:
            log_f.write(str(search_key_dict)+str(len(search_key_dict))+'\n')
        if len(search_key_dict) == 0:
            return render_template('search.html',noresult=True)
        #正则表达式模糊搜索
        search_result = []
        #with open('test.txt','w') as f:
        #    f.write(str(names_exist))
        for name in names_exist:
            if name != '.name_list':
                #(search_key.lower() in name.lower() )
                with open(name+'.txt','r') as f:
                    entry = eval(f.read())
                def isQualified(entry):
                    for key in search_key_dict:
                        try:
                            if not(search_key_dict[key].lower() in entry[key].lower()):
                                return False
                        except KeyError:
                            return False
                    else:
                        return True
                if isQualified(entry):
                    search_result.append(entry)
                #with open('test.txt','w') as f:
                #    f.write(str(search_result))
        if search_result != []:
            return render_template('search.html',results = search_result)
        else:
            return render_template('search.html',noresult=True)


if __name__ == '__main__':
    app.run(debug=True)

#  **kwargs  (keyword argument)

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
func(first_name='astha',last_name='bhardwaj')

def name(**kwargs):
    # print(num,kwargs)
    for k,v in kwargs.items():
        print(f"{k}:{v}")
        # print(k,v)
num={'name':'astha bhardwaj', 'age':20,'height_in_cm':164}
# name('astha',first_name='astha',last_name='bhardwaj')
name(**num) #unpacking

'''
function with all parameters

we have to write in this format

    parameters
    *args
    default parameter
    **kwargs

'''

def func (name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
func('astha',1,2,3,a=1,b=2)

#question
def func (l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
    
names=['astha','ravita']
print(func(names,reverse_str=True))
        
def func (l,**kwargs):
    for name in l:
        if kwargs.get('reverse_str')==True:
            print(name[::-1].title())
        else:
            print(name.title())
    
names=['astha','ravita']
func(names,reverse_str=True)  #The print(func(...)) statement will print None because the func function does not return anything


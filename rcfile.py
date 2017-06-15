class Singleton(object):
  """
  Class implementing the Singleton design pattern. There are several ways to implement
  the singleton pattern in python. The most elegant way is to use the decorators but such
  construct has been introduced only starting from python 2.6
  """
  def __new__(cls, *args, **kwds):
    if not '_the_instance' in cls.__dict__:
      cls._the_instance =  object.__new__(cls)
      cls._the_instance.init(*args, **kwds)
    return cls._the_instance
  def init(self, *args, **kwds):
    pass

class rcfile(Singleton) :
   """class to handle an rc file"""
   def init(self,inputString,isHereDoc=False) :
      for k in (\
               open(inputString,'r') \
            if hereDoc else (\
                  inputString.split('\n') 
               if type() == type('') else \
                  inputString \
                  )
               ):
         l=k.strip()
         if len(l) > 0 :
            if l[0]!='#' :
               ll=l.split('=')
               self[ll[0].strip()]=ll[1].strip() if ll[1].strip()!='' else None
   def copy(self) :
      import copy
      return copy.deepcopy(self)
   def keys(self) :
      return self.__dict__.keys()
   def __setitem__(self,this,that) :
      self.__dict__[this]=that
   def __getitem__(self,this) : 
      if len(self.__dict__) == 0 : return
      return self.__dict__[this]

# libbottles
A python library for interacting with Bottles.  

## Examples
### Create new bottle
```python
from libbottles.manager import Manager

Manager.create_bottle(
    env=2,
    path="/full/bottle/path",
    name="Merlot",
    runner_path="/full/runner/path",
    versioning=False,
    verbose=0
)
```

### List bottles
```python
Manager.update_bottles()
bottles = Manager.get_bottles()

for b in bottles:
    print(b.config)
```

## Purpose
libbottles (currently a concept), should be used to create new Bottles 
clients and _**should not be used to interact with Wine**_.  

Soon this library will offer all the features to interact with bottles 
(which are not standard wineprefix) like:
- list bottles
- get bottle details
- edit bottle settings (both wine and software specific)
- versioning
- components management (runners, dxvk, ..)
- software dependencies management
- installers management
- and more.. (all you can do today in Bottles and more)

### Best practices
If you want to create a Bottles client you have to use libbottles, all the 
functionalities that interact with the bottles must come from the library and 
not be hard-scripted.  

If a feature is missing you can collaborate to integrate it into libbottles, I 
repeat do not hard-script anything in your client because that change may be 
useful to other developers, also you could break future compatibility with the 
bottle configuration model.

**Can I use libbottles to manage wine/wineprefix in my application?**  
No, or rather yes, but it would be better not. If your purpose is to work with 
Wine or wineprefixes in general, you should use the 
[libwine](https://github.com/bottlesdevs/libwine) library. This 
offers a number of methods to create and manage a wineprefix.

**Can I use libwine to creare 3rd party Bottles clients?**  
No. Seriously, don't do this. If you want to create a Bottles client, you 
should use libbottles, thus taking advantage of the official methods to access 
and manage your bottles in the system.

**Ok. Why?**  
By using libbottles we make sure we offer a development standard and 
encourage them to work together to improve a single foundation.

**It is not too much?**  
No, we don't believe. Bottles is a hobby made with passion but everyone has 
their own commitments and it is important to manage the project in the best way 
right away to avoid having to get your hands on multiple projects, each with 
a different code base, methods and logics.
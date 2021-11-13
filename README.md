# What is Minicord?
> Minicord is a open source replica of discord. I originally started working on this as I was bored at home one time. This is completely free to take and to work on. 
> Minicord has complete customization from top to bottom coming to creating servers and customizing them via the console.

## Me and my friend have Minicord how do I add them?
> tl;dr the answer is you cant

The 3 main reasons why you are unable to do this is because;
1. I'd have to set up a server to handle messages and image sending (way to much effort for me)
2. If you want to message them use discord. Minicord is a *Mini*-replica of discord, so functions like that Im not going to implement.
3. **no**

## I want to suggest something how?
You could either.
1. Click the suggest button on Minicord
2. Open a *Issue* and give it the **request** tag
3. If you'd perfer not to feel free to message a Project Designer on [Discord](https://discord.com/invite/6AkXb5rRW7)

## Whare are your future plans with Minicord?
> In all honestly I have no idea. I started it for fun but I've become attached to this project and I want to continue it. Soooooo... I'll probably keep working on it for the time being...
I mean if you got a offer... **hmu**

# Extra

## How do I create my own server on Minicord?
**The only current way to create your own server is:**
```python
create_server(MiniCordUI, True, 'Name', 'Description')
Name.config('Minicord Server.')
Description.config('Minicord Description.')
Name.apply(True, True)
Description.apply(True, 1)
# Patched should have worked
```

| Command | Description |
| ------- | ----------- |
| Name | Configs the default server name |
| Description | Configs the default server about me |
| Icon | Configs the default server icon |
| Everyoneperm | Configs everyones perms |
| Rolecolor | Configs the role color #hex |

Please create a *Issue* Request If you recieve any errors.

## How do I customize the Minicord default colors?
```python
Reconfig.colors(default1, 'blue')
Reconfig.colors(default2, 'orange')
Reconfig.colors(default3, default)
```
**This will be the outcome**
![image](https://user-images.githubusercontent.com/80045521/141642155-8fcfec60-2d5f-4f74-a53a-5147c72052ed.png)
> It doesn't look nice but what ever floats your boat.

## How do I change the message at the top left?
```python
TitleText = 'whatever'
reload()
```
> Change "whatever" with anything you wish.





## What is Minicord?
> Minicord is a open source replica of discord. I originally started working on this as I was bored at home one time. This is completely free to take and to work on. 
> Minicord as complete customization from top to bottom coming to creating servers and customizing them via the console.

## How do I create my own server on Minicord?
> The only current way to create your own server is:
```python
create_server(MiniCordUI, True, 'Name', 'Description')
Name.config('Minicord Server.')
Description.config('Minicord Description.')
Name.apply(True, True)
Description.apply(True, 1)
# Patched should have worked
```

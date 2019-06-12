# windowo pop

弹窗提示

# usage

```python

self.env['window.pops'].create({
    "name":"your pop up window's title",
    "text": "message to users"
}).get_action()
```

注意，不能使用装饰器@api.one装饰。

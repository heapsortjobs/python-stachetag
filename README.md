python-stachetag
================

Implement stachetags in your Pythons lickety-split.

## Stachetags?

[http://blog.heapsortjobs.com/stachetags-we-have-the-solution](http://blog.heapsortjobs.com/stachetags-we-have-the-solution)

## ITS SO EASY

```
>>> import stachetag
>>> stachestring = "This string{ has multiple{ stachetags{ in it!"

>>> waxer = stachetag.StacheWaxer(stachestring)

>>> waxer.get_tags()
['string', 'multiple', 'stachetags']

>>> waxer.get_stachetags()
['string{', 'multiple{', 'stachetags{']

>>> for stache in waxer:
...     print stache
...
<stachetag.StacheTag object at 0x102e87650>
<stachetag.StacheTag object at 0x102e87710>
<stachetag.StacheTag object at 0x102e87750>

>>> waxer.format_staches(format_string="<a href='#{tag}'>{stachetag}</a>")
"This <a href='#string'>string{</a> has <a href='#multiple'>multiple{</a> <a href='#stachetags'>stachetags{</a> in it!"
```

## Contribute!

Pull requests welcome.  Integrations encouraged.  Shaving is frowned upon.

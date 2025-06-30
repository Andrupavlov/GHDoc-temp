# Markdown Syntax:
Information taken from this resource: [Guide to Markdown](https://markdown.rozh2sch.org.ua/#%D0%B3%D0%BE%D1%80%D0%B8%D0%B7%D0%BE%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0-%D0%BB%D1%96%D0%BD%D1%96%D1%8F)

## 1. Text

*Italic*  _text_

**Bold**  __text__

==Highlighted text==

~~Strikethrough text~~

```markdown
*Italic*  _text_

**Bold**  __text__

==Highlighted text==

~~Strikethrough text~~
```

## 2. Quote (Callouts)

Regular quote syntax without colored border:
```markdown
> Quote text.
```

> Quote text

Syntax with colored border and specific status:
```markdown
>[!note] note
```

>[!note]
>note - for general notes or additional information

> [!tip] 
> tip - for useful tips or recommendations

> [!important]
> important - for highlighting important information

> [!warning] 
> warning - for warning about potential problems

> [!caution] 
> caution - for calling for caution

## 3. Lists

* item 1
* item 2
    * nested item 2.1
    * nested item 2.2
* item 3
	+ nested item 3.1
	+ nested item 3.2
	    - nested item 3.2.1
	    - nested item 3.2.2

1. Item 1
2. Item 2
    1. Nested item 2.1 
    2. Nested item 2.2
3. Item 3

```markwodn
* item 1
* item 2
    * nested item 2.1
    * nested item 2.2
* item 3
	+ nested item 3.1
	+ nested item 3.2
	    - nested item 3.2.1
	    - nested item 3.2.2

1. Item 1
2. Item 2
    1. Nested item 2.1 
    2. Nested item 2.2
3. Item 3
```

## 5. Links

This is a [link](https://example.com).
```markdown
This is a [link](https://example.com).
```

This is a [link with title attribute](https://example.com "I am a link")
This is - [without title](https://example.com)
```markdown
This is a [link with title attribute](https://example.com "I am a link"). 
This is - [without title](https://example.com).
```

https://www.example.com
```markdown
https://www.example.com
```

example@hotmail.com
<example@hotmail.com>
```markdown
example@hotmail.com
<example@hotmail.com>
```

## 6. Images 

![alt](https://bit.ly/33B4VxM "shih-tzu")

## 7. Code

```
// code block
var foo = 'bar';
```

```javascript
// JavaScript code highlighting
var foo = 'bar';
```

```javascript
// JavaScript code highlighting
var foo = 'bar';
```

## 8. Table 

Product    | Price
---------- | -----
Laptop     | $1600
Smartphone | $150
Printer    | $75

> Use the : (colon) symbol for table alignment.


| Name           | Surname   |        Development |
| :------------- | :-------: | ----------------: |
| left aligned   | centered  | right aligned     |
| Linus          | Torvalds  |            Linux  |
| Dennis         |   Ritchie |                 C |
| Jack           |   Dorsey  |          Twitter  |


## 14. Special Characters

In Markdown, you can use several special characters for formatting and iconography. Below are the main symbols and constructions that may be useful.

### 14.1. Arrows

In Markdown, regular text characters can automatically convert to special characters or arrows:

`-> <-` → (arrow)

`<->` ↔ (bidirectional arrow)

`<= =>` ⇐ => (implication arrow)

`<=>`  ⇔ (logical equality)

### 14.2. Symbols

Unicode symbols, so you can use them for insertion:

✔ (checkmark): U+2714

✖ (cross): U+2716

➔ (large arrow): U+2794

🔗 (link): Unicode or insertion via emoji.

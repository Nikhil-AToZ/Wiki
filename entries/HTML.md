# HTML
---
## Introduction

HTML, which stands for **HyperText Markup Language**, is the standard markup language used to structure content on the web.

HTML defines the structure of a webpage using elements such as headings, paragraphs, links, images, lists, forms, tables, and other content.

HTML is not a programming language because it does not contain programming logic such as loops or functions. Instead, it describes the structure and meaning of web content.

## History

HTML was created by **Tim Berners-Lee** while working at CERN. The first version of HTML was introduced in the early 1990s as part of the development of the World Wide Web.

HTML has evolved through several versions. Modern websites primarily use **HTML5**, which introduced many semantic elements and features designed for modern web applications.

## Basic Structure

A basic HTML document has a structure similar to this:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>

    <h1>Hello World</h1>
    <p>This is my webpage.</p>

</body>
</html>
```

The main parts are:

- `<!DOCTYPE html>` tells the browser that the document uses HTML5.
- `<html>` is the root element.
- `<head>` contains information about the document.
- `<title>` defines the browser tab title.
- `<body>` contains the visible webpage content.

## HTML Elements

HTML documents are built using elements.

```html
<p>This is a paragraph.</p>
```

Here, `<p>` is the opening tag and `</p>` is the closing tag.

Some elements do not require a closing tag.

```html
<img src="image.jpg" alt="A picture">


These are commonly called void elements.

## Headings

HTML provides six heading levels:

##html
<h1>Main Heading</h1>
<h2>Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Heading</h4>
<h5>Heading</h5>
<h6>Heading</h6>


`<h1>` represents the highest-level heading, while `<h6>` represents the lowest level.

Headings help organize the structure of a document.

## Paragraphs

Paragraphs are created using the `<p>` element.

```html
<p>
    HTML is used to structure content on a webpage.
</p>
```

## Links

The `<a>` element creates hyperlinks.

```html
<a href="https://example.com">Visit Website</a>
```

The `href` attribute specifies the destination of the link.

Links can also point to another page within the same website:

```html
<a href="/about">About</a>
```

## Images

Images are added using the `<img>` element.

```html
<img src="photo.jpg" alt="A photograph">
```

Important attributes include:

- `src` - specifies the image location.
- `alt` - provides alternative text describing the image.

The `alt` attribute is important for accessibility and when an image cannot be displayed.

## Lists

HTML supports ordered and unordered lists.

### Unordered List

```html
<ul>
    <li>Python</li>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

### Ordered List

```html
<ol>
    <li>Learn HTML</li>
    <li>Learn CSS</li>
    <li>Learn JavaScript</li>
</ol>
```

The `<li>` element represents an individual list item.

## Tables

Tables are used to represent structured tabular data.

```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>

    <tr>
        <td>Nikhil</td>
        <td>18</td>
    </tr>
</table>
```

Common table elements include:

- `<table>` - creates the table.
- `<tr>` - creates a row.
- `<th>` - creates a header cell.
- `<td>` - creates a data cell.

## Forms

HTML forms allow users to enter and submit information.

```html
<form>
    <label for="name">Name:</label>

    <input type="text" id="name" name="name">

    <button type="submit">Submit</button>
</form>
```

Forms can contain different types of controls, including:

- Text inputs
- Password inputs
- Checkboxes
- Radio buttons
- Select menus
- Text areas
- Buttons

## Attributes

Attributes provide additional information about HTML elements.

For example:

```html
<a href="/about" class="link">About</a>
```

Here:

- `href` specifies the link destination.
- `class` identifies the element for CSS and JavaScript.

Common attributes include:

```text
id
class
href
src
alt
title
name
value
type
```

## Semantic HTML

Semantic HTML uses elements that describe the meaning of their content.

Examples include:

```html
<header>
    Website Header
</header>

<nav>
    Navigation
</nav>

<main>
    Main Content
</main>

<section>
    A Section
</section>

<article>
    An Article
</article>

<footer>
    Website Footer
</footer>
```

Semantic elements make the structure of a webpage easier to understand for developers, browsers, search engines, and assistive technologies.

## `<div>` and `<span>`

`<div>` is a generic block-level container.

```html
<div class="card">
    <h2>Python</h2>
    <p>A programming language.</p>
</div>
```

`<span>` is a generic inline container.

```html
<p>
    This is <span class="highlight">important</span>.
</p>
```

These elements are commonly used when a more specific semantic element is not appropriate.

## HTML Comments

Comments can be added using:

```html
<!-- This is a comment -->
```

Comments are not displayed as visible content on the webpage.

## HTML and CSS

HTML provides the structure of a webpage, while CSS controls its appearance.

For example:

```html
<h1 class="title">Hello World</h1>
```

CSS can then style the element:

```css
.title {
    font-size: 40px;
    text-align: center;
}
```

A useful way to think about their roles is:

```text
HTML → Structure
CSS  → Appearance
JavaScript → Behavior
```

## HTML and JavaScript

JavaScript can interact with HTML elements and change the webpage dynamically.

For example:

```html
<button id="button">Click Me</button>

<script>
    document.getElementById("button").onclick = function() {
        alert("Hello!");
    };
</script>
```

HTML creates the button, while JavaScript adds behavior to it.

## HTML5

HTML5 is the modern version of HTML and introduced many useful features and semantic elements.

Examples include:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<footer>`
- `<video>`
- `<audio>`
- `<canvas>`

HTML5 also provides better support for modern web applications and multimedia.

## Accessibility

HTML plays an important role in making websites accessible.

Good practices include:

- Using semantic HTML.
- Providing `alt` text for meaningful images.
- Using labels for form controls.
- Maintaining a logical heading structure.
- Making interactive elements usable with keyboards.

For example:

```html
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

The label clearly describes the purpose of the input.

## HTML in Web Development

HTML is one of the core technologies of the web.

A typical frontend uses:

```text
HTML
 │
 ├── Structure
 │
 ├── CSS
 │    └── Styling
 │
 └── JavaScript
      └── Interactivity
```

Backend technologies such as Django, Flask, or Node.js can generate or serve HTML pages to users.

## Advantages

- Easy to learn
- Supported by all modern web browsers
- Provides the basic structure of webpages
- Works together with CSS and JavaScript
- Supports semantic and accessible web development
- Essential for frontend web development

## Limitations

- HTML alone cannot provide advanced styling.
- HTML alone cannot provide complex application logic.
- Interactive behavior usually requires JavaScript.
- Large documents can become difficult to maintain without good structure and organization.

## Conclusion

HTML is the fundamental markup language of the web. It defines the structure and meaning of content displayed by web browsers.

Although HTML does not provide the complete functionality of a modern website by itself, it forms the foundation on which CSS, JavaScript, and backend technologies are built.

Understanding HTML is therefore an essential first step in learning web development.

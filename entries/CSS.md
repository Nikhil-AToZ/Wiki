# CSS
---
## Introduction

CSS, which stands for **Cascading Style Sheets**, is a stylesheet language used to control the appearance and layout of HTML documents.

CSS can be used to control:

- Colors
- Fonts
- Spacing
- Borders
- Layout
- Animations
- Responsive design

## Basic Syntax

A CSS rule consists of a selector and a declaration block.

```css
p {
    color: blue;
    font-size: 18px;
}
```

Here, `p` is the selector and the properties define how paragraphs should look.

## Selectors

Selectors are used to choose HTML elements.

```css
p {
    color: black;
}

.card {
    padding: 20px;
}

#header {
    background-color: black;
}
```

CSS selectors can target elements, classes, IDs, attributes, and different states of elements.

## Colors and Text

CSS controls the appearance of text and backgrounds.

```css
.title {
    color: #333333;
    font-size: 40px;
    font-family: Arial, sans-serif;
    text-align: center;
}
```

Common text properties include `font-size`, `font-weight`, `line-height`, `letter-spacing`, and `text-decoration`.

## Box Model

The CSS box model describes how the size and spacing of elements are calculated.

```text
Margin
 └── Border
      └── Padding
           └── Content
```

Example:

```css
.card {
    width: 300px;
    padding: 20px;
    border: 1px solid black;
    margin: 20px;
}
```

Understanding the box model is important when creating layouts.

## Flexbox

Flexbox is a layout system designed for arranging elements in rows or columns.

```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
}
```

It is commonly used for navigation bars, buttons, cards, and other components.

## Grid

CSS Grid is designed for two-dimensional layouts.

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

Grid is useful for page layouts and collections of cards.

## Responsive Design

Responsive design allows websites to adapt to different screen sizes.

```css
@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr;
    }
}
```

Media queries allow different styles to be applied depending on the viewport.

## Pseudo-classes

Pseudo-classes style elements according to their state.

```css
button:hover {
    background-color: black;
    color: white;
}
```

Common pseudo-classes include `:hover`, `:focus`, `:active`, and `:first-child`.

## Transitions and Animations

Transitions create smooth changes between styles.

```css
button {
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: black;
}
```

CSS also supports animations using `@keyframes`.

## HTML and CSS

HTML provides structure while CSS provides presentation.

```text
HTML → Structure
CSS  → Styling
JavaScript → Behavior
```

CSS can be placed in an HTML document or loaded as an external stylesheet.

```html
<link rel="stylesheet" href="style.css">
```

## Advantages

- Separates structure from presentation
- Supports responsive layouts
- Provides powerful layout systems
- Supports transitions and animations
- Makes consistent styling easier

## Limitations

- Large stylesheets can become difficult to maintain.
- Browser differences sometimes require testing.
- Complex layouts require a good understanding of the box model and layout systems.

## Conclusion

CSS is one of the core technologies of web development. It transforms HTML structure into a visually organized and responsive interface.

Learning selectors, the box model, Flexbox, Grid, positioning, and responsive design provides a strong foundation for modern frontend development.

# CSS

CSS stands for **Cascading Style Sheets**. It is a stylesheet language used to control the appearance and layout of HTML documents.

HTML defines the structure of a webpage, while CSS controls how that structure looks.

CSS is one of the three core technologies used to build websites, along with HTML and JavaScript.

## What CSS Does

CSS can control many visual properties of a webpage.

Some common uses of CSS include:

- Changing colors
- Changing fonts
- Setting widths and heights
- Adding margins and padding
- Creating borders
- Changing backgrounds
- Positioning elements
- Creating responsive layouts
- Creating animations
- Designing navigation bars
- Creating grids and columns

## CSS Syntax

A CSS rule usually consists of a selector and a declaration block.

    selector {
        property: value;
    }

For example:

    p {
        color: red;
        font-size: 18px;
    }

Here, `p` is the selector.

`color` and `font-size` are properties.

`red` and `18px` are the values assigned to those properties.

A CSS file can contain many rules, each targeting different HTML elements.

## Adding CSS to HTML

There are three common ways to add CSS to an HTML document.

### Inline CSS

CSS can be written directly inside an HTML element.

    <p style="color: red;">Hello World</p>

Inline CSS is simple for small changes, but it is generally not recommended for large projects because it makes HTML harder to maintain.

### Internal CSS

CSS can be written inside a `<style>` element in the HTML document.

    <style>
        p {
            color: red;
        }
    </style>

### External CSS

CSS is commonly stored in a separate file.

    styles.css

The stylesheet can then be connected to an HTML document.

    <link rel="stylesheet" href="styles.css">

External stylesheets are generally preferred because they keep the structure and presentation separate.

## CSS Selectors

Selectors are used to choose which HTML elements should receive a style.

### Element Selector

An element selector targets HTML elements directly.

    h1 {
        color: green;
    }

This changes the color of every `<h1>` element.

### Class Selector

A class selector starts with a period.

    .container {
        width: 80%;
    }

It can be applied to an HTML element using the `class` attribute.

    <div class="container">
        Content
    </div>

Multiple elements can use the same class.

### ID Selector

An ID selector starts with a hash symbol.

    #header {
        background-color: black;
    }

It can be used with:

    <div id="header">
        Header
    </div>

IDs are normally intended to uniquely identify an element on a page.

## Grouping Selectors

Multiple selectors can be grouped together.

    h1, h2, h3 {
        font-family: Arial, sans-serif;
    }

This applies the same styles to all three heading types.

## Descendant Selectors

A selector can target elements inside another element.

    .container p {
        color: blue;
    }

This targets paragraphs that are descendants of an element with the `container` class.

## The Cascade

The word "cascading" in CSS refers to the process used by the browser to determine which styles should be applied when multiple rules affect the same element.

For example:

    p {
        color: blue;
    }

    p {
        color: red;
    }

The later rule can override the earlier rule when both have the same specificity.

The cascade depends on factors such as importance, specificity, and source order.

## Specificity

Specificity determines which CSS selector has greater priority.

A general order of specificity is:

1. Element selectors
2. Class and attribute selectors
3. ID selectors
4. Inline styles

For example:

    p {
        color: blue;
    }

    .text {
        color: green;
    }

    #important {
        color: red;
    }

An element matching all three selectors will generally receive the color from the most specific selector.

## Comments

CSS comments can be written using `/* */`.

    /* This is a CSS comment */

Comments are ignored by the browser and can be used to explain sections of CSS.

## Colors

CSS provides several ways to specify colors.

A color name can be used:

    body {
        color: black;
    }

Hexadecimal values can also be used:

    body {
        background-color: #ffffff;
    }

RGB values are another option:

    body {
        background-color: rgb(255, 255, 255);
    }

RGBA can also specify transparency:

    body {
        background-color: rgba(255, 255, 255, 0.5);
    }

## Backgrounds

CSS can control the background of an element.

    body {
        background-color: lightgray;
    }

Images can also be used as backgrounds.

    body {
        background-image: url("background.jpg");
    }

Other background properties can control size, position, and repetition.

## Fonts

CSS can control the font used by an element.

    body {
        font-family: Arial, sans-serif;
    }

Font size can be changed using the `font-size` property.

    h1 {
        font-size: 36px;
    }

Text can also be made bold.

    strong {
        font-weight: bold;
    }

Font style can be changed as well.

    em {
        font-style: italic;
    }

## Text

CSS provides several properties for controlling text.

    p {
        text-align: center;
        line-height: 1.6;
        letter-spacing: 1px;
    }

The `text-align` property controls horizontal alignment.

The `line-height` property controls the vertical spacing between lines.

The `letter-spacing` property controls the space between characters.

## The Box Model

Every HTML element can be thought of as a rectangular box.

The CSS box model consists of:

1. Content
2. Padding
3. Border
4. Margin

### Content

The content is the actual text, image, or other material inside an element.

### Padding

Padding creates space inside an element between the content and its border.

    .box {
        padding: 20px;
    }

### Border

A border surrounds the content and padding.

    .box {
        border: 1px solid black;
    }

### Margin

Margin creates space outside an element.

    .box {
        margin: 20px;
    }

## Width and Height

CSS can control the dimensions of elements.

    .box {
        width: 300px;
        height: 200px;
    }

Percentages can also be used.

    .box {
        width: 80%;
    }

Viewport units are useful for responsive layouts.

    .box {
        width: 50vw;
        height: 50vh;
    }

## Box Sizing

The `box-sizing` property controls how an element's width and height are calculated.

A commonly used setting is:

    * {
        box-sizing: border-box;
    }

With `border-box`, padding and borders are included in the specified width and height.

## Display

The `display` property determines how an element participates in layout.

Common values include:

- `block`
- `inline`
- `inline-block`
- `flex`
- `grid`
- `none`

For example:

    .hidden {
        display: none;
    }

This removes the element from the page layout.

## Positioning

CSS provides several positioning methods.

    .box {
        position: relative;
    }

Common position values include:

- `static`
- `relative`
- `absolute`
- `fixed`
- `sticky`

For example:

    .menu {
        position: fixed;
        top: 0;
        right: 0;
    }

A fixed element remains positioned relative to the viewport.

## Flexbox

Flexbox is a CSS layout system designed for arranging elements in rows or columns.

A flex container can be created using:

    .container {
        display: flex;
    }

The `gap` property can add space between elements.

    .container {
        display: flex;
        gap: 20px;
    }

Elements can be centered using:

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

`justify-content` controls alignment along the main axis.

`align-items` controls alignment along the cross axis.

## CSS Grid

CSS Grid is another layout system.

A grid can be created using:

    .container {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }

This creates two equal columns.

Multiple columns can be created using:

    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }

Grid is especially useful for layouts that require rows and columns.

## Responsive Design

Responsive design allows websites to adapt to different screen sizes.

Media queries can apply different styles depending on the screen width.

    @media (max-width: 600px) {
        .container {
            width: 100%;
        }
    }

This allows a webpage to change its layout when viewed on smaller screens.

Responsive design is especially important for mobile devices.

## Units

CSS supports many different units.

Common absolute units include:

- `px`
- `pt`
- `cm`
- `mm`

Common relative units include:

- `%`
- `em`
- `rem`
- `vw`
- `vh`

For example:

    .box {
        width: 50%;
        font-size: 1rem;
    }

Relative units are often useful when creating responsive interfaces.

## Pseudo-Classes

Pseudo-classes allow styles to be applied when an element is in a particular state.

For example, the `:hover` pseudo-class can change the appearance of a link when the mouse is placed over it.

    a:hover {
        text-decoration: underline;
    }

Other common pseudo-classes include:

- `:focus`
- `:active`
- `:visited`
- `:first-child`
- `:last-child`

## Pseudo-Elements

Pseudo-elements allow specific parts of an element to be styled.

For example:

    p::first-letter {
        font-size: 30px;
    }

The `::before` and `::after` pseudo-elements can also insert generated content.

    .box::before {
        content: "Start";
    }

## Borders

CSS can control the appearance of borders.

    .box {
        border: 2px solid black;
    }

Different sides can be styled separately.

    .box {
        border-top: 2px solid black;
        border-bottom: 2px solid black;
    }

Border radius can create rounded corners.

    .box {
        border-radius: 10px;
    }

## Shadows

CSS can create shadows around elements.

    .box {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

Text can also have shadows.

    h1 {
        text-shadow: 2px 2px 4px gray;
    }

## Transitions

Transitions allow CSS property changes to happen gradually.

    button {
        background-color: blue;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: green;
    }

This creates a smoother visual change when the button is hovered.

## Animations

CSS can create animations using `@keyframes`.

    @keyframes example {
        from {
            opacity: 0;
        }

        to {
            opacity: 1;
        }
    }

The animation can then be applied to an element.

    .box {
        animation: example 2s;
    }

Animations can be useful for visual feedback and interface effects, but excessive animation can make a website distracting.

## Variables

CSS variables allow values to be reused.

    :root {
        --main-color: blue;
        --spacing: 20px;
    }

They can then be used with the `var()` function.

    .button {
        color: var(--main-color);
        padding: var(--spacing);
    }

Variables make large stylesheets easier to maintain.

## Overflow

The `overflow` property controls what happens when content is larger than its container.

    .box {
        overflow: hidden;
    }

Other common values include:

- `visible`
- `hidden`
- `scroll`
- `auto`

## Z-Index

The `z-index` property controls the stacking order of positioned elements.

    .front {
        position: relative;
        z-index: 10;
    }

An element with a higher `z-index` can appear above an element with a lower stacking order when the relevant positioning and stacking context rules allow it.

## Accessibility

CSS should be written with accessibility in mind.

Avoid relying only on color to communicate information.

For example, instead of making an error message only red, also provide meaningful text.

    .error {
        color: red;
        font-weight: bold;
    }

Focus indicators should also remain visible so keyboard users can understand which element is currently selected.

## CSS Best Practices

Some useful CSS practices include:

- Use meaningful class names.
- Keep CSS organized.
- Avoid unnecessary duplication.
- Prefer external stylesheets for larger projects.
- Use responsive units when appropriate.
- Avoid excessive use of `!important`.
- Keep specificity manageable.
- Test layouts on different screen sizes.
- Consider accessibility when designing interfaces.
- Use reusable classes and CSS variables where appropriate.

## CSS and HTML

HTML and CSS have different responsibilities.

HTML describes the structure and content of a webpage.

For example:

    <button>Submit</button>

CSS controls how that button appears.

    button {
        background-color: blue;
        color: white;
        padding: 10px 20px;
    }

Keeping structure and presentation separate makes websites easier to develop and maintain.

## CSS and JavaScript

JavaScript can interact with CSS to create dynamic interfaces.

For example, JavaScript can add or remove a CSS class from an element.

    element.classList.add("active");

The CSS can then define what the `active` class looks like.

    .active {
        display: block;
    }

This allows JavaScript to control visual states without manually changing every CSS property.

## Advantages of CSS

CSS provides several important advantages:

- It separates presentation from document structure.
- Styles can be reused across many pages.
- It supports responsive layouts.
- It provides powerful layout systems such as Flexbox and Grid.
- It supports animations and transitions.
- It allows websites to adapt to different devices.
- It reduces the need for presentation-related HTML attributes.

## Limitations and Challenges

CSS can also become difficult to manage in large projects.

Common challenges include:

- Complex specificity rules
- Conflicting styles
- Large and difficult-to-maintain stylesheets
- Browser differences
- Responsive design complexity
- Unexpected layout behavior
- Managing many reusable components

Using consistent naming conventions, reusable styles, and a clear project structure can help reduce these problems.

## Conclusion

CSS is a fundamental technology for web development.

It controls the visual presentation and layout of HTML documents.

Understanding selectors, the cascade, specificity, the box model, positioning, Flexbox, Grid, responsive design, and accessibility provides a strong foundation for working with CSS.

CSS becomes much more powerful when combined with HTML and JavaScript to create interactive and responsive web applications.
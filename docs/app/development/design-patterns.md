---
cover: >-
  https://bs-uploads.toptal.io/blackfish-uploads/components/blog_post_page/content/cover_image_file/cover_image/1303284/regular_1708x683_cover-comprehensive-guide-javascript-design-patterns-cf0c7c0e69d51d97044a8431da9175e3.png
coverY: 0
---

# 🎯 Design Patterns

In the Mercado Topográfico App project, we defined some project standards to be followed by all developers on the team.

## Folder Organization

![Image title](../../files/image (2).png)

Each folder is responsible for managing a specific part of the project:

### App

The 'app' folder is where the page with the components should be mounted. The 'app' folder is where the page with the components should be mounted. There should be an 'index.tsx' file and an 'index.style.ts' file for page styling.

![Image title](../../files/image (3).png)

There are also some **layout files**, you can check more in this documentation:

```embed
url: https://docs.expo.dev/routing/layouts/
```

### Commons

The 'commons' folder has two subdirectories (for better organization) and both are responsible for managing the application context, taking information from one component to the other. Find out more in this article:

```embed
url: https://react.dev/reference/react/createContext
```

![Image title](../../files/image (4).png)

### Components

This is where the application components are located. You should group them according to what you are building, or if it is something that will be reused in other pages and components, you should add them to the 'commons' folder:

![Image title](../../files/image (5).png)

### Hooks

For the sake of organization, we chose to separate the logic from the component. This folder is where the logical part is:

![Image title](../../files/image (6).png)

### Service

This is where we connect to the API:

![Image title](../../files/image (7).png)

### Types

This is where we set up the object interface:

![Image title](../../files/image (8).png)

### Utils

Utility functions or reusable information are here:

![Image title](../../files/image (9).png)

## Nomenclature

There is a standard to be followed when naming folders, files, functions, etc.

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>Folders</td><td><strong>my-folder</strong></td><td>Kebab Case</td></tr><tr><td>Files (For Components)</td><td><strong>index.tsx</strong></td><td></td></tr><tr><td>Files (For Component Styling)</td><td><strong>index.style.ts</strong></td><td></td></tr><tr><td>Component Function</td><td><strong>MyComponent</strong></td><td>Pascal Case</td></tr><tr><td>Interfaces</td><td><strong>InterfaceName</strong></td><td>Pascal Case</td></tr><tr><td>General Function</td><td><strong>myFunctionName</strong></td><td>Camel Case</td></tr><tr><td>Variables and Const</td><td><strong>myConst</strong></td><td>Camel Case</td></tr><tr><td>Custom Hooks</td><td><strong>useHookName</strong></td><td>Camel Case and starting with "use"</td></tr><tr><td>Test Folder</td><td><strong>__tests__</strong></td><td>This name exactly</td></tr><tr><td>Importing Style</td><td><strong>import * as Style from "./index.style"</strong></td><td></td></tr><tr><td>Using Style</td><td><strong>&#x3C;Style.ComponentName.Item /></strong></td><td></td></tr><tr><td>Const for Style</td><td><strong>StyleName</strong></td><td>PascalCase</td></tr></tbody></table>

## Creation Functions

### For Component

:white\_check\_mark: Accepted

```javascript
export const DepartmentCarousel = () => {
    // your code
}
```

:x: Not Accepted

```javascript
export function DepartmentCarousel() {
    // your code
}
```

### For Pages

:white\_check\_mark: Accepted

```javascript
export default function Index() {
  return (
    <>
      // your code
    </>
  )
}
```

:x: Not Accepted

```javascript
export default const Index = () => {
  return (
    <>
      // your code
    </>
  )
}
```


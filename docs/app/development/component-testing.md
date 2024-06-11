---
cover: >-
  https://assets-global.website-files.com/619e15d781b21202de206fb5/62f62b00791f0a712a693a46_Core-Benefits-of-Automated-Testing-in-App-Development.webp
coverY: 0
---

# 🧪 Component Testing

Following good programming practices, it is recommended to carry out a test for each component created.

In the project, we are using the React Native Testing Library. You can find more details on this page:

{% embed url="https://github.com/callstack/react-native-testing-library" %}

Inside the component directory, create a folder \_\_**tests\_\_** and add a file **index.test.tsx**&#x20;

![Image title](../../files/image (33).png)

You must do **at least 1 happy path test and 1 edge case test**, for example:

```javascript
// TEST FOR DEPARTMENT CAROUSEL COMPONENT
describe("Department Carousel", () => {

  // TEST 1 - HAPPY PATH
  it("Render the department carousel with its categories", () => {
    const { isLoading, redirect, mockCategories } = setup()
    const { getAllByTestId } = render(
      <DepartmentCarousel
        categories={mockCategories}
        isLoading={isLoading}
        redirect={redirect}
      />
    )
    expect(getAllByTestId("department-container")).toBeTruthy()
  })
  
  // TEST 2 - EDGE CASE
  it("should render DepartmentCarouselSkeleton when categories are loading", () => {
    const { loadingSkeleton, redirect, mockCategories } = setup()
    const { getAllByTestId } = render(
      <DepartmentCarousel
        categories={mockCategories}
        isLoading={loadingSkeleton}
        redirect={redirect}
      />
    )
    expect(getAllByTestId("department-skeleton")).toBeTruthy()
  })
  
})
```

{% hint style="danger" %}
Run the component test every time you finish it. Don't wait to finish all the component tests to do this.
{% endhint %}

![Image title](../../files/image (34).png)

After you finish all the testing of the component you created, run all the application tests to make sure nothing is breaking.

![Image title](../../files/image (35).png)

![Image title](../../files/image (36).png)

### Codium AI for Testing

Codium is a great tool to help you create tests. Although it is not 100% accurate in some cases, it helps you gain more agility when setting up your component tests. You have to install the extension in your IDE:

{% embed url="https://www.codium.ai/" %}

#### Codium for WebStorm

File -> Settings

![Image title](../../files/image (37).png)

Plugins -> Search for "Codium" -> Install

![Image title](../../files/image (38).png)

Now, you can generate automated tests with the help of AI:

![Image title](../../files/image (39).png)

![Image title](../../files/image (40).png)


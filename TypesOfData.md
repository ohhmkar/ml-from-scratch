#### ML Learning - Omkar Gajare

## Types of data

When working with datasets, data can come in different forms.

Understanding the type of data helps us decide how to preprocess and use it in ML models.

1. ## Numerical Data (Quantitative)
   Data represented as numbers.

Age = 25 → **Discrete**

Salary = $55,000 → **Discrete**

```
Clarification: You might think salary could be continuous, but in practice, it's paid in specific currency units (e.g., dollars and cents). Since there are finite, countable steps between values (you can't be paid $55,000.12345), we treat it as discrete.
```

Weight = 72.8 kg → **Continuous**

2. ## Categorical Data (Qualitative)
   Data represented as categories or labels.

- Gender = {Male, Female, Other} → Unordered
- Department = {HR, IT, Finance} → Unordered
- Customer Satisfaction = {Low, Medium, High} → Ordered

3. ## Text Data
   Data in the form of sentences, paragraphs, or words.

- Reviews: "This product is amazing!"
- Tweets, comments, articles.

4. ## Image Data
   Data in the form of pictures or visuals. To a computer, an image is a grid of pixels, where each pixel has a numerical value representing its color and intensity.

- Handwritten digit images
- Medical scans (X-rays, MRIs)
- Satellite photos for weather prediction
- Product photos on an e-commerce site
- Security camera footage

### MCQ

Q. A health-tracking app records the number of steps a user takes in a day. Sometimes a person may walk 5,000 steps, other times 12,300 steps. The values are always whole counts.

```
Numerical (Discrete)
```

Q. A university collects data about students’ blood groups for medical records. Possible values are {A, B, AB, O}. There is no ranking or priority among these categories.

```
Categorical (Unordered)
```

Q. Researchers collect thousands of tweets about a new smartphone launch. Each tweet is a short text message, often with slang, hashtags, or emojis.

```
Text
```

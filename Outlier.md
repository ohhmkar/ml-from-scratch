#### ML Learning - Omkar Gajare

## Outliers

> What is Outlier

An outlier is a value in your data that is very different from the other values.<br>
Think of it like a<b> “weird guest”</b>in a group: they just don’t fit in with the rest.

Example:
<br>We have a dataset of students’ test scores:

| Sr No | Name  | Score |
| ----- | ----- | ----- |
| 1     | Alice | 50    |
| 2     | Bob   | 52    |
| 3     | Carol | 49    |
| 4     | Dave  | 51    |
| 5     | Eve   | 100   |

Most scores are around 50, but Eve scored 100, that’s an outlier.
<br><b><i>Note: Outliers are easy to see when you look at the data or plot it on a graph.</b></i>

> Why Outliers Matter

Outliers can change the average a lot.

- They can confuse machine learning models, especially if the model expects “normal” values.
- Sometimes outliers are mistakes in data, and sometimes they are real but rare events.

Example:
<br>Average score without Eve: `(50+52+49+51)/4 = 50.5`
<br>Average score with Eve:` (50+52+49+51+100)/5 = 60.4` →<b><i> big jump because of one outlier!</b></i>

> How to Handle Outliers Once we spot an outlier, we decide what to do with it:

| Method    | What it Means                                | Example with Eve’s Score |
| --------- | -------------------------------------------- | ------------------------ |
| Leave it  | Keep it if it’s real and important           | Keep 100                 |
| Remove it | Delete if it’s a mistake                     | Remove 100               |
| Adjust it | Replace with a nearby value to reduce impact | Change 100 → 52          |

<b><i>
Note: Always ask why the outlier exists before deciding what to do.

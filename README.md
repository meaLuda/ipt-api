# IMAGE PREPROCESSING AS A SERVICE TOOL FOR BUILDERS | DEVELOPERS (WebApp)

```text
The aim of this project is to create a plug-and-play API-as-a-service for 
image preprocessing and later on machine learning and deep-learning too
```

---

```R
TODO:                                               Deadline        Done? 
- Create Image preprocessing tools (2 to 3)        11/02/22         [  ]         

```

---

<h1> Helper Links & Notes </h1>

[Creating a Data Pipeline with EasyJobs & FastAPI](https://medium.com/analytics-vidhya/creating-a-data-pipeline-with-easyjobs-fastapi-4e302556f05d#:~:text=Creating%20a%20Data%20Pipeline%20with%20EasyJobs%20%26%20FastAPI,...%207%20Task%20Flow%20...%208%20Conclusion%20)

[ML Pipeline Tutorial](https://www.youtube.com/watch?v=CApCQKuWqBM&ab_channel=CodingEntrepreneurs)

[How you can quickly deploy your ML models with FastAPI](https://towardsdatascience.com/how-you-can-quickly-deploy-your-ml-models-with-fastapi-9428085a87bf)

[Image Processing Using Numpy: With Practical Implementation And Code](https://www.analyticsvidhya.com/blog/2021/05/image-processing-using-numpy-with-practical-implementation-and-code/#:~:text=It%20is%20used%20in%20the,%2DImage%2C%20and%20many%20more.)

---

<h2> Code Snippets </h2>

```python
# ?? should we consider chunking of > 100 images | multithreading rather than a loop. ??
images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    img = Image.open(image)
    # image manipulation functions/functionalities.
    img.thumbnail((600,600))
    img.save("resized_"+image, optimize=True, quality=40)
```

# CourseScope

Topic modelling for university courses using clustering techniques, with the intent of providing intuitive analytics of course schedules. This NLP model groups courses into similar areas of interests based on significant keywords extracted using TF-IDF vectors.

The sample dataset present was scrapped from Stanford's CS courses using Beautiful Soup, and is used for non-commercial purposes. (https://explorecourses.stanford.edu/search?page=0&catalog=&q=CS&view=catalog&filter-catalognumber-CS=on)

After removing common stop words from the course descriptions, Sklearn is mainly used to vectorize the text inputs, and then clustered based on cosine distances.
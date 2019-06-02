## Introduction

This is a website based on Django and Vue.js. Version now v-1.0.
You can use it [by click here](http://www.rdworkspace.com/)

### Function

It can calculate recipe's and assessment's nutrients. Recipes are bind with patients, you should write down patients' information and then initialize a assessment. In the futrue, this web application can add pack a PDF file which is patient's nutrition report.

### API

Application refers restful-api, you can easily use it.

```
# login
https: www.rdworkspace.com/lab_api/login/  # require post username and password in json to get token

# food database
https: www.rdworkspace.com/lab_api/food/  # require get and post methods
https: www.rdworkspace.com/lab_api/food/<food_id> # you can get, put, or delete through this

# patients' information
https: www.rdworkspace.com/lab_api/patient/ # require get and post methods
https: www.rdworkspace.com/lab_api/patient/<patient_id> # you can get, put, or delete through this

# assessment
https: www.rdworkspace.com/lab_api/assessment/ # require get and post methods
https: www.rdworkspace.com/lab_api/assessment/<assessment_id>/ #  require get method to get detail informations

...
```

### changelog

- firstly deploy by chengyuan 2019.6.2
- init project 2019.5.25

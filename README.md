# iReporter Application

## Description
### An application that allows users to anonymously upload and repoert problems with reference to corruption and other malpractices in the government. 

## Specifications
1. _A user sign up and login functionality_
2. _Ability to report problems observed in the general public_
3. _USer profile display with user details_
4. _Administrators page that allows tracking of reports_
5. _Ability to delete and check on changes uploaded_

### Installing

*Step 1*

Create directory
```$ mkdir iReporter```

```$ cd iReporter```

Create and activate virtual environment

```$ virtualenv env -p python3```


```$ source env/bin/activate ```

Clone the repository [```here```](https://github.com/charliekaks/iReporter.git) or 

``` git clone https://github.com/charliekaks/iReporter.git ```

Install project dependencies 


```$ pip install -r requirements.txt```


*Step 2* 

#### Set up database and virtual environment & Database 

``` No database setup required, the app uses data-structures to store data```


#### Running the application

```$ flask run``` 

*Step 3*

#### Testing

```$ pytest```

### API-Endpoints

#### Red Flag Endpoints : api/v1/redflags

Method | Endpoint | Functionality
--- | --- | ---
POST | /api/v1/red-flags | Create a red flag
GET | /api/v1/red-flags/id | Get a specific red flag
PATCH| /api/v1/red-flags/id/comment | Change a particular comment
PATCH | /api/v1/red-flags/id/location | Change a particular comment
DELETE | /api/v1/red-flags/id | Delete a red flag


## Link to Live site
[iReporter live site]()
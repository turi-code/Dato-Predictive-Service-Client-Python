Dato Predictive Service Python Client
=====================================

The purpose of the Dato Predictive Service Python Client library is to allow
Python applications to easily query Dato Predictive Services.

Installation
------------

To install Dato Predictive Service Python Client, simply:

.. code-block:: bash

    sudo pip install dato-predictive-service-client

or from source:

.. code-block:: bash

    sudo python setup.py install

Requirements
------------

- Dato Predictive Service, launched by GraphLab-Create >= 1.4 installation

Usage
-----

Create Client
^^^^^^^^^^^^^

To use the Dato Predictive Service Python Client, first you need to obtain the
following information from a running Dato Predictive Service:

- Predictive Service CNAME or DNS name (endpoint)
- API key from the Predictive Service

Once you have obtained the above information, simply create a new PredictiveServiceClient:

.. code-block:: python
    
    from dato.deploy import PredictiveServiceClient;

    client = PredictiveServiceClient(endpoint = <endpoint>,
                                    api_key = <api_key>,
                                    should_verify_certificate = <True-or-False>)

To enable SSL certificate verification for this Predictive Service, 
set the ``should_verify_certificate`` to **true**. However, if your Predictive Service
is launched with a self-signed certificate or without certificate, please 
set ``should_verify_certificate`` to **false**.

The PredictiveServiceClient can also be created by using a Predictive Service `client configuration file`_.

.. code-block:: python

    client = PredictiveServiceClient(config_file = <path_to_file>)

Query
^^^^^

To query a model that is deployed on the Predictive Service, you will need:

- model name
- method to query (recommend, predict, query, etc.)
- data used to query against the model

For example, the code below demonstrates how to query a recommender model, named
``rec``, for recommendations for user ```Jacob Smith```:

.. code:: python

    data = {'users': ['Jacob Smith'] }
    result = client.query('rec', method = 'recommend', data = data)

**Notes**

- Different models could support different query methods (recommend, predict, query, etc.)
  and different syntax and format for **data**. You will need to know the
  supported methods and query data format before querying the model.

Set timeout
^^^^^^^^^^^

To change the request timeout when querying the Predictive Service, use the following:

.. code:: python

    # set timeout to 5 seconds.
    client.set_query_timeout(timeout = 5)

The default timeout is 10 seconds.

Results
^^^^^^^

The output to the ``query()`` function is a dictionary of the query result.

If query is successful, the query result contains:

- model response
- uuid for this query
- version of the model

.. code:: python

    model_response = result['response']
    uuid = result['uuid']
    version = result['version']

``model_response`` contains the actual model output from your query.

Send feedback
^^^^^^^^^^^^^

Once you get the query result, you can submit feedback data corresponding to this query
back to the Predictive Service. This feedback data can be used for evaluating your
current model and training future models.

To submit feedback data corresponding to a particular query, you will need the UUID
of the query. The UUID can be easily obtained from the query result.

.. code:: python

    uuid = result['uuid']

For the feedback data, you can use any attributes or value pairs that you like.

Example: 

.. code:: python

    feedback_data = dict()
    feedback_data['num_of_clicks'] = 3
    feedback_data['searched_terms'] = 'test'

Now we can send this feedback data to the Predictive
Service to associate this feedback with a particular query.

.. code:: python

    client.feedback(uuid, feedback_data);

More Info
---------

For more information about the Dato Predictive Service, please read
the `API docs`_ and `userguide`_.

License
-------

The Dato Predictive Service Python Client is provided under the 3-clause BSD `license`_.


.. _client configuration file: https://dato.com/products/create/docs/generated/graphlab.deploy.PredictiveService.save_client_config.html
.. _API docs: https://dato.com/products/create/docs/generated/graphlab.deploy.PredictiveService.html 
.. _userguide: https://dato.com/learn/userguide/deployment/pred-getting-started.html
.. _license: https://github.com/dato-code/Dato-Predictive-Service-Client-Python/raw/master/LICENSE 

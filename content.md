# Auth

How you verified that the user can use your resources

## Basic auth

Is a user:password value that'll be included in the headers of all the requests

## Session auth

Once you know the session or cookie. You can send the session.

## Bearer Token

Is the REST standard.

Because REST is stateless, you'll need to know on each request the information of the user

## Token auth

Request will need a header call Authentication

# Implementation of token authentication in Django

## With RestFramework

You need to install the `"rest_framework.authtoken"` and include the `"rest_framework.authentication.TokenAuthentication"` class in the `DEFAULT_AUTHENTICATION_CLASSES` optino

And then you can generate tokens inside the auth token.
You'll include it in the headers as `Token THIS_IS_THE_TOKEN`

## JSON_WEB_TOKEN

Is a token that it's cypher

It won't touch the models. So you can keep it as stateless

These tokens have an expiry date

## Which information you'll include in this token

Most of the time:

- userId
- name of user
- iat: `meaning=issued at` so you can define if it is expired or not

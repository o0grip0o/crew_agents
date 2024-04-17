#!/bin/zsh

# variables
model_name="llama2:13b"
custom_model_name="crewai-llama"

# get the base model
ollama pull $model_name

# create the model file
ollama create $custom_model_name -f ./Llama2ModelFile

# remove the base model
ollama rm $model_name
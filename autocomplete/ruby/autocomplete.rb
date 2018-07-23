#!/usr/bin/env ruby

require "json"
require "sinatra"

# Install with:
#   gem install sinatra rerun

# Run with:
#   rerun 'ruby autocomplete.rb'

set :public_folder, File.dirname(__FILE__) + "./"

get "/helloworld" do
  "hello world"
end

get "/" do
  # Main entry point.
  send_file File.expand_path("static/autocomplete.html", settings.public_folder)
end

get "/search" do
  query = params["q"]
  headers "Content-Type" => "application/json"
  JSON.generate({:query => query, :results => ["result 1", "result 2"]})
end

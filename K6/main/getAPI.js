import http from "k6/http";
import { sleep } from "k6";

export const options = {
  vus: 50, //virtual user
  duration: "30s",
cloud: {
    // Project: Default project
    projectID: 4650521,
    // Test runs with the same name groups test runs together.
    name: 'Test (28/09/2025-01:55:08)'
  }
};

export default function () {
  http.get("https://www.automationexercise.com/");
  sleep(1);
}

// local run: k6 run K6/main/getAPI.js
// cloud run (grafana): k6 cloud K6/main/getAPI.js

//check """test_results1.pdf""" for the results
#!/usr/bin/env sh
set -e

# Used for debugging if no foreground application is being called
# while true; do
#    echo "Financial operation processor: $(date)"
#    sleep 5
# done

NOW=$(date +%Y%m%d%H%M%S)

if [ ${TEST_MODE} = "True" ]; then
    reports_dir="../output/tests reports"
    feature_reports_dir="${reports_dir}/feature/${NOW}"
    tests_dir="../tests"

    cd ./application

    python3.12 -m pytest -vv --cov=. --cov-report html:"${reports_dir}"/unit/${NOW}/coverage/ --html="${reports_dir}"/unit/${NOW}/report.html "${tests_dir}"/unit

    mkdir -p "${feature_reports_dir}" && python3.12 -m robot -d "${feature_reports_dir}" "${tests_dir}"/feature
else
    ./application/financial_operation_processor.py < ./data/operations
fi 

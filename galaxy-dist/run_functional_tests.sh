#!/bin/sh

# A good place to look for nose info: http://somethingaboutorange.com/mrl/projects/nose/
rm -f run_functional_tests.log 

if [ ! $1 ]; then
	python ./scripts/functional_tests.py -v --with-nosehtml --html-report-file run_functional_tests.html --exclude="^get" functional
elif [ $1 = 'help' ]; then
	echo "'run_functional_tests.sh'                          for testing all the tools in functional directory"
	echo "'run_functional_tests.sh aaa'                      for testing one test case of 'aaa' ('aaa' is the file name with path)"
	echo "'run_functional_tests.sh -id bbb'                  for testing one tool with id 'bbb' ('bbb' is the tool id)"
	echo "'run_functional_tests.sh -sid ccc'                 for testing one section with sid 'ccc' ('ccc' is the string after 'section::')"
	echo "'run_functional_tests.sh -list'                    for listing all the tool ids"
	echo "'run_functional_tests.sh -toolshed'                for running all the test scripts in the ./test/tool_shed/functional directory"
	echo "'run_functional_tests.sh -toolshed testscriptname' for running one test script named testscriptname in the .test/tool_shed/functional directory"
    echo "'run_functional_tests.sh -workflow test.xml'       for running a workflow test case as defined by supplied workflow xml test file"
	echo "'run_functional_tests.sh -framework'               for running through example tool tests testing framework features in test/functional/tools"    
	echo "'run_functional_tests.sh -framework -id toolid'    for testing one framework tool (in test/functional/tools/) with id 'toolid'"
	echo "'run_functional_tests.sh -data_managers -id data_manager_id'    for testing one Data Manager with id 'data_manager_id'"
elif [ $1 = '-id' ]; then
	python ./scripts/functional_tests.py -v functional.test_toolbox:TestForTool_$2 --with-nosehtml --html-report-file run_functional_tests.html
elif [ $1 = '-sid' ]; then
        python ./scripts/functional_tests.py --with-nosehtml --html-report-file run_functional_tests.html -v `python tool_list.py $2`
elif [ $1 = '-list' ]; then
        python tool_list.py
	echo "==========================================================================================================================================="
	echo "'run_functional_tests.sh -id bbb'               for testing one tool with id 'bbb' ('bbb' is the tool id)"
	echo "'run_functional_tests.sh -sid ccc'              for testing one section with sid 'ccc' ('ccc' is the string after 'section::')"
elif [ $1 = '-migrated' ]; then
    if [ ! $2 ]; then
        python ./scripts/functional_tests.py -v functional.test_toolbox --with-nosehtml --html-report-file run_functional_tests.html -migrated
    elif [ $2 = '-id' ]; then
        # TODO: This option is not tested...
        python ./scripts/functional_tests.py -v functional.test_toolbox:TestForTool_$3 --with-nosehtml --html-report-file run_functional_tests.html -migrated
    else
        python ./scripts/functional_tests.py -v functional.test_toolbox --with-nosehtml --html-report-file run_functional_tests.html -migrated
    fi
elif [ $1 = '-installed' ]; then
    if [ ! $2 ]; then
        python ./scripts/functional_tests.py -v functional.test_toolbox --with-nosehtml --html-report-file run_functional_tests.html -installed
    elif [ $2 = '-id' ]; then
        # TODO: This option is not tested...
        python ./scripts/functional_tests.py -v functional.test_toolbox:TestForTool_$3 --with-nosehtml --html-report-file run_functional_tests.html -installed
    else
        python ./scripts/functional_tests.py -v functional.test_toolbox --with-nosehtml --html-report-file run_functional_tests.html -installed
    fi
elif [ $1 = '-toolshed' ]; then
    if [ ! $2 ]; then
        python ./test/tool_shed/functional_tests.py -v --with-nosehtml --html-report-file ./test/tool_shed/run_functional_tests.html ./test/tool_shed/functional
    else
        python ./test/tool_shed/functional_tests.py -v --with-nosehtml --html-report-file ./test/tool_shed/run_functional_tests.html $2
    fi
elif [ $1 = '-workflow' ]; then
    python ./scripts/functional_tests.py -v functional.workflow:WorkflowTestCase --with-nosehtml --html-report-file ./test/tool_shed/run_functional_tests.html -workflow $2
elif [ $1 = '-data_managers' ]; then
    if [ ! $2 ]; then
        python ./scripts/functional_tests.py -v functional.test_data_managers --with-nosehtml --html-report-file run_functional_tests.html -data_managers
    elif [ $2 = '-id' ]; then
        python ./scripts/functional_tests.py -v functional.test_data_managers:TestForDataManagerTool_$3 --with-nosehtml --html-report-file run_functional_tests.html -data_managers
    else
        python ./scripts/functional_tests.py -v functional.test_data_managers --with-nosehtml --html-report-file run_functional_tests.html -data_managers
    fi
elif [ $1 = '-framework' ]; then
    if [ ! $2 ]; then
        python ./scripts/functional_tests.py -v functional.test_toolbox --with-nosehtml --html-report-file run_functional_tests.html -framework
    elif [ $2 = '-id' ]; then
        python ./scripts/functional_tests.py -v functional.test_toolbox:TestForTool_$3 --with-nosehtml --html-report-file run_functional_tests.html -framework
    else
        echo "Invalid test option selected, if -framework first argument to $0, optional second argument must be -id followed a tool id."
    fi
else
	python ./scripts/functional_tests.py -v --with-nosehtml --html-report-file run_functional_tests.html $1
fi

echo "'run_functional_tests.sh help'                  for help"

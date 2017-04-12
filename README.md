#A Log combiner and processor: translogrify

Translogrify is designed to limit the deluge of log emails that occurs in technical emails. 

## How it works

Rather than have individual alerts send emails on their own, translogrify collects each alert into a row of a table along with a severity code and a list of its intended recipents. On demand, emails can then be sent per-recipient with a given lookback and severity level.

## Installation

Translogrify can be installed from github: 

    git clone git@github.com:asteriske/translogrify.git ~/translogrify

    pip install ~/translogrify

After installing, update ~/.translogrify.conf with settings appropriate to your environment:

    [DEFAULT]
    mailfromaddr = fromaddr
    mysqlpass = mysqlpass
    mailpass = mailpass
    table = log
    mysqlhost = mysqlhost
    mysqluser = mysqluser
    db = translogrify 
    mailserver = server

Currently TLS on port 587 is assumed. 

Assign a MySQL user with CREATE privileges and then run 

    $ create_db_and_table

which will create the log db as specified in `.translogrify.conf`. 

## Usage

A new line is added to the log with an invocation like the following:

    log_update MESSAGE ALERT_LEVEL EMAIL1 EMAIL2 ...

To send email digests to each user with their messages from the last 12 hours with severity >= 3,

    send_tgy_email --lookback 96 --minlevel 3

Each recipient will then get a color-coded priority-sorted email like this:


<table id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" none="">
<thead>
<tr>
<th class="blank level0">
<th class="col_heading level0 col0" colspan="1">
                  date
                
                
                
                <th class="col_heading level0 col1" colspan="1">
                  level
                
                
                
                <th class="col_heading level0 col2" colspan="1">
                  message
                
                
            </th></th></th></th></tr>
</thead>
<tbody>
<tr>
<th class="row_heading level0 row0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    13
                
                
                
                <td class="data row0 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow0_col0">
                    2017-04-01 22:06:45
                
                
                
                <td class="data row0 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow0_col1" style="background-color: red; color: white">
                    5
                
                
                
                <td class="data row0 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow0_col2">
                    ERROR: EVERYTHING BROKEN 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    10
                
                
                
                <td class="data row1 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow1_col0">
                    2017-04-01 22:01:37
                
                
                
                <td class="data row1 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow1_col1" style="background-color: red; color: white">
                    5
                
                
                
                <td class="data row1 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow1_col2">
                    ERROR: Other stuff broken too 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    1
                
                
                
                <td class="data row2 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow2_col0">
                    2017-04-01 19:04:36
                
                
                
                <td class="data row2 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow2_col1" style="background-color: orange; color: white">
                    4
                
                
                
                <td class="data row2 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow2_col2">
                    ALERT: Config file missing for the thing 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row3" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    7
                
                
                
                <td class="data row3 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow3_col0">
                    2017-04-01 22:01:06
                
                
                
                <td class="data row3 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow3_col1" style="background-color: yellow; color: black">
                    3
                
                
                
                <td class="data row3 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow3_col2">
                    Sevice foo exited with state 3 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row4" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    5
                
                
                
                <td class="data row4 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow4_col0">
                    2017-04-01 19:31:10
                
                
                
                <td class="data row4 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow4_col1" style="background-color: yellow; color: black">
                    3
                
                
                
                <td class="data row4 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow4_col2">
                    Sevice foo exited with state 3 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row5" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    3
                
                
                
                <td class="data row5 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow5_col0">
                    2017-04-01 19:29:43
                
                
                
                <td class="data row5 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow5_col1" style="background-color: yellow; color: black">
                    3
                
                
                
                <td class="data row5 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow5_col2">
                    Sevice foo exited with state 3 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row6" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    2
                
                
                
                <td class="data row6 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow6_col0">
                    2017-04-01 19:28:40
                
                
                
                <td class="data row6 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow6_col1" style="background-color: yellow; color: black">
                    3
                
                
                
                <td class="data row6 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow6_col2">
                    Unauthorized login attempt on localhost 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row7" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    0
                
                
                
                <td class="data row7 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow7_col0">
                    2017-04-01 19:04:27
                
                
                
                <td class="data row7 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow7_col1" style="background-color: green; color: white">
                    2
                
                
                
                <td class="data row7 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow7_col2">
                    Backup service approaching quota 
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row8" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    28
                
                
                
                <td class="data row8 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow8_col0">
                    2017-04-04 03:00:23
                
                
                
                <td class="data row8 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow8_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row8 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow8_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row9" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    27
                
                
                
                <td class="data row9 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow9_col0">
                    2017-04-04 02:25:19
                
                
                
                <td class="data row9 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow9_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row9 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow9_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row10" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    26
                
                
                
                <td class="data row10 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow10_col0">
                    2017-04-04 02:20:19
                
                
                
                <td class="data row10 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow10_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row10 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow10_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row11" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    25
                
                
                
                <td class="data row11 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow11_col0">
                    2017-04-04 02:15:19
                
                
                
                <td class="data row11 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow11_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row11 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow11_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row12" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    24
                
                
                
                <td class="data row12 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow12_col0">
                    2017-04-04 02:10:18
                
                
                
                <td class="data row12 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow12_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row12 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow12_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row13" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    23
                
                
                
                <td class="data row13 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow13_col0">
                    2017-04-03 21:23:55
                
                
                
                <td class="data row13 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow13_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row13 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow13_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row14" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    22
                
                
                
                <td class="data row14 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow14_col0">
                    2017-04-03 21:23:11
                
                
                
                <td class="data row14 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow14_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row14 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow14_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row15" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    21
                
                
                
                <td class="data row15 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow15_col0">
                    2017-04-03 21:03:49
                
                
                
                <td class="data row15 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow15_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row15 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow15_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row16" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    20
                
                
                
                <td class="data row16 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow16_col0">
                    2017-04-01 23:08:49
                
                
                
                <td class="data row16 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow16_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row16 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow16_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row17" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    19
                
                
                
                <td class="data row17 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow17_col0">
                    2017-04-01 23:03:04
                
                
                
                <td class="data row17 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow17_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row17 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow17_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
<tr>
<th class="row_heading level0 row18" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05eb" rowspan="1">
                    18
                
                
                
                <td class="data row18 col0" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow18_col0">
                    2017-04-01 22:55:05
                
                
                
                <td class="data row18 col1" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow18_col1" style="background-color: white; color: black">
                    1
                
                
                
                <td class="data row18 col2" id="T_c5be92ca_18ea_11e7_9063_b827eb2c05ebrow18_col2">
                    DynDNS is set properly
                
                
            </td></td></td></th></tr>
</tbody>
</table>

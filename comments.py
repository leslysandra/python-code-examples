
# avoid obvious comment

# not this
// get the country code
$country_code = get_country_code($_SERVER['REMOTE_ADDR']);
 
// if country code is US
if ($country_code == 'US') {
 
    // display the form input for state
    echo form_input_state();
}


# better this
// display state selection for US users
$country_code = get_country_code($_SERVER['REMOTE_ADDR']);
if ($country_code == 'US') {
    echo form_input_state();
}

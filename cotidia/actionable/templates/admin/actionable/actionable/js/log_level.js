function (value) {
    cls = "primary"
    if (value == "WARNING") cls = "warning";
    if (value == "ERROR") cls = "danger";
    return { __html: '<span class="label label--' + cls + '">' + value + '</span>' }
}
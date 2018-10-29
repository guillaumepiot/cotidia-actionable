function (value) {
    cls = "label--danger"
    if (value == "SOLVED") cls = "label--success";
    if (value == "IGNORED") cls = "";
    return { __html: '<span class="label ' + cls + '">' + value + '</span>' }
}

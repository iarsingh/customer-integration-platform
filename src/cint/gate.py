class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("mapping"): failed.append("mapping")
    if not body.get("sandbox_ok"): failed.append("sandbox")
    return {"passed": not failed, "failed": failed, "applied": False}

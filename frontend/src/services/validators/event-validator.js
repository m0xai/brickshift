export function requiredRule(val) {
	return !!val || "This field is required";
}

export function dayRule(val) {
	return (
		/^-?[\d]+-[0-1]\d-[0-3]\d$/.test(val) ||
		"You should provide a valid date value, like 2023-11-15 (YYYY-MM-DD)"
	);
}

export function timeRule(val) {
	return (
		/^([0-1]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?$/.test(val) ||
		"You should provide a valid time value, like 14:30"
	);
}

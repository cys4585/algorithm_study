function solution(new_id) {
	let answer = '';
	
	// step 1
	new_id = new_id.toLowerCase();
	// step 2
	new_id = new_id.replace(/[^a-z0-9-_.]/g, '');
	// step 3
	new_id = new_id.split('');
	new_id = new_id.filter((val, idx) => {
	  if (idx + 1 === new_id.length) return true;
	  if (val === '.' && val === new_id[idx + 1]) return false;
	  return true;
	})
	// step 4
	if (new_id[0] === '.') new_id.shift();
	if (new_id[new_id.length - 1] === '.') new_id.pop();
	// step 5
	if (new_id.length === 0) new_id = ["a"];
	// step 6
	if (new_id.length > 15) new_id.splice(15);
	if (new_id[new_id.length - 1] === '.') new_id.pop();
	// step 7
	if (new_id.length < 3) {
	  let length = new_id.length;
	  for(let i = 0; i < 3 - length; i++) {
		new_id.push(new_id[length - 1]);
	  }
	}
	answer = new_id.join('');
	return answer;
}
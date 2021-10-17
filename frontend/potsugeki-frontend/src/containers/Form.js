import { useState } from 'react'
import './Form.css'
import axios from 'axios'

function Form() {

	const [name,setName] = useState('')
	const [url,setUrl] = useState('')
	const [recipe,setRecipe] = useState('')
	const [tags,setTags] = useState('')

	async function handleSubmit(e) {
		e.preventDefault();
		const payload = JSON.stringify({
			"name": name,
			"url": url,
			"recipe": recipe,
			"tags": tags.split(',').length > 0 ? tags.split(',') : ''
		})
		const res = await axios.post("https://potsugeki-z7qgr7dfca-uc.a.run.app/new_clip/kobai", payload, {
			headers: {
				'Content-Type': 'application/json'
			}
		})
		console.log(res.data)
		setName('')
		setUrl('')
		setRecipe('')
		setTags('')
	}

	return (
		<form className='form_container'>
			<input placeholder='Clip Name' className='text_area' value={name} onChange={e=>setName(e.target.value)}/>
			<input placeholder='Twitter Clip Url' className='text_area' value={url} onChange={e=>setUrl(e.target.value)}/>
			<input placeholder='Combo Recipe' className='text_area' value={recipe} onChange={e=>setRecipe(e.target.value)}/>
			<input placeholder='Tags' className='text_area' value={tags} onChange={e=>setTags(e.target.value)}/>
			<div>
				<input className='submit_button' type='submit' onClick={handleSubmit}/>
			</div>
		</form>
	)
}

export default Form
import { TwitterTweetEmbed } from 'react-twitter-embed'
import './Card.css'
import axios from 'axios'

function Card(props) {

	async function handleDelete(e){
		e.preventDefault()
		const res = await axios.delete(`https://potsugeki-z7qgr7dfca-uc.a.run.app/delete/kobai/${props.props.id}`)
		window.location.reload(false)
	}

	return (
		<div className='card_container'>
			<div>
				<button className='delete_button' onClick={handleDelete}>X</button>
			</div>
			<div className='meta_container'>
				<div className='title'>{props.props.name}</div>
				{props.props.recipe !== '' &&
					<div className='recipe'>{props.props.recipe}</div>
				}
				<div className='tag_container'>
					{props.props.tags.map(item => <span className='tag'>{item}</span>)}
				</div>
			</div>
			<div className='clip_container'>
				<TwitterTweetEmbed
					tweetId={props.props.url}
				/>
			</div>
		</div>
	)
}

export default Card
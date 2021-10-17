import { TwitterTweetEmbed } from 'react-twitter-embed'
import './Card.css'

function Card(props) {
	console.log(props)
	return (
		<div className='card_container'>
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
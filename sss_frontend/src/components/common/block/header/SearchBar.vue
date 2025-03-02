<template>
    <form class="form-inline search-full col" action="#" method="get">
        <div class="form-group w-100">
            <div class="Typeahead Typeahead--twitterUsers">
                <div class="u-posRelative">
                    <input class="demo-input Typeahead-input form-control-plaintext w-100" type="text"
                        placeholder="Search Mofi ..">
                    <div class="spinner-border Typeahead-spinner" role="status"><span class="sr-only">Loading...</span>
                    </div><vue-feather class="close-search" type="x"></vue-feather>
                </div>
                <div class="Typeahead-menu"></div>
            </div>
        </div>
    </form>
</template>
